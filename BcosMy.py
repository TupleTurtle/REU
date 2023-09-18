import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.ops import DeformConv2d, deform_conv2d


class NormLinear(nn.Linear):
    def forward(self, x):
        w = F.normalize(self.weight, p=2, dim=-1)
        return F.linear(x, w)
    

class BLinear(nn.Module):
    def __init__(self, inp, out, maxout=1):
        super().__init__()
        self.o = out
        self.linear = NormLinear(inp, out*maxout, bias=False)
        self.m = maxout
        self.detach = False
        self.register_buffer('gamma', torch.tensor([90.]))

    def forward(self, x):
        out = self.linear(x)

        if self.m >1 :
            out = out.unflatten(-1, (self.o, self.m))
            out = out.max(-1).values
        
        norm = torch.linalg.vector_norm(x, dim=-1, keepdim=True) + 1e-12
        mout = out

        if self.detach:
            norm = norm.detach()
            mout = mout.detach()
        
        scale = mout.abs() / norm

        return scale * out * self.gamma
    

class NormConv2d(nn.Conv2d):
    def forward(self, x):
        w = F.normalize(self.weight, p=2, dim=(1, 2, 3))
        return self._conv_forward(x, w, None)
    

class BConv2d(nn.Module):
    def __init__(self, inp, out, kern=3, pad=1, stride=1, maxout=1):
        super().__init__()
        self.conv = NormConv2d(inp, out*maxout, kern, stride, pad, bias=False)
        self.pad = pad
        self.kern = kern
        self.stride = stride
        self.wind = kern**2
        self.m = maxout
        self.o = out
        self.detach = False
        self.register_buffer('gamma', torch.tensor([90.]))

    def forward(self, x):
        out = self.conv(x)

        if self.m > 1:
            out = out.unflatten(1, (self.o, self.m))
            out = out.max(2).values

        norm = (x**2).sum(1, keepdim=True)
        norm = (F.avg_pool2d(norm, self.kern, self.stride, self.pad, divisor_override=1) + 1e-6).sqrt_()
        mout = out

        if self.detach:
            norm = norm.detach()
            mout = out.detach()

        scale = mout.abs() / norm
        
        return scale * out * self.gamma
    


class BConv2dGroup(nn.Module):
    def __init__(self, inp, out, groups, kern=3, pad=1, stride=1, maxout=1):
        super().__init__()
        self.conv = NormConv2d(inp, out*maxout, kern, stride, pad, groups=groups, bias=False)
        self.G = groups
        self.C = inp//groups 
        self.O = out
        self.pad = pad
        self.kern = kern
        self.stride = stride
        self.wind = kern**2
        self.m = maxout
        self.o = out
        self.detach = False
        self.register_buffer('gamma', torch.tensor([90.]))

    def forward(self, x):
        out = self.conv(x)

        if self.m > 1:
            out = out.unflatten(1, (self.o, self.m))
            out = out.max(2).values

        norm = (x**2).unflatten(1, (self.G, self.C)).sum(2)
        norm = (F.avg_pool2d(norm, self.kern, self.stride, self.pad, divisor_override=1) + 1e-6).sqrt_()
        norm = norm.repeat_interleave(repeats=self.O//self.G, output_size=self.O, dim=1)
        mout = out

        if self.detach:
            norm = norm.detach()
            mout = out.detach()

        scale = mout.abs() / norm
        
        return scale * out * self.gamma
    

class Bconv2dPoint(nn.Module):
    def __init__(self, inp, out, maxout=1):
        super().__init__()
        self.w = nn.Parameter(torch.randn(out*maxout, inp, 1, 1))
        self.m = maxout
        self.o = out
        self.detach = False
        self.register_buffer('gamma', torch.tensor([90.]))

    def forward(self, x):
        w = F.normalize(self.w, p=2, dim=1)
        out = F.conv2d(x, w)

        if self.m > 1:
            out = out.unflatten(1, (self.o, self.m))
            out = out.max(2).values

        norm = torch.linalg.vector_norm(x, dim=1, keepdim=True) + 1e-12
        mout = out

        if self.detach:
            norm = norm.detach()
            mout = mout.detach()

        scale = mout.abs() / norm
        
        return scale * out * self.gamma
    


class PLU(nn.Module):
    def __init__(self, p, init):
        super().__init__()
        self.pr = nn.PReLU(p, init)
    def forward(self, x):
        return self.pr(x.mT).mT
    

class MLP(nn.Sequential):
    def __init__(self, emb, expansion, maxoutOut=1, maxoutIn=1):
        super().__init__()
        hid = emb * expansion
        self.add_module('fc1', BLinear(emb, hid, maxoutIn))
        #self.add_module('dp1', nn.Dropout(inplace=True))
        self.add_module('relu', nn.LeakyReLU(inplace=True))
        self.add_module('fc2', BLinear(hid, emb, maxoutOut))
        #self.add_module('dp2', nn.Dropout(inplace=True))



class MLPC(nn.Sequential):
    def __init__(self, emb, expansion, maxoutOut=1, maxoutIn=1):
        super().__init__()
        self.hid = emb * expansion
        self.add_module('fc1', Bconv2dPoint(emb, self.hid, maxoutIn))
        self.add_module('relu', nn.LeakyReLU(inplace=True))
        self.add_module('fc2', Bconv2dPoint(self.hid, emb, maxoutOut))



class LNorm2d(nn.Module):
    def __init__(self, emb, dims=(1, 2, 3)):
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(1, emb, 1, 1))
        self.dims = dims
        self.detach = False

    def forward(self, x):
        var, mean = torch.var_mean(x, dim=self.dims, unbiased=False, keepdim=True)

        if self.detach:
            var = var.detach()

        std = (var + 1e-5).sqrt_()

        result = self.gamma * ((x - mean) / std)
        
        return result
    


class LNorm1d(nn.Module):
    def __init__(self, emb, dims=(-1, -2)):
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(emb))
        self.dims = dims
        self.detach = False

    def forward(self, x):
        var, mean = torch.var_mean(x, dim=self.dims, unbiased=False, keepdim=True)

        if self.detach:
            var = var.detach()

        std = (var + 1e-5).sqrt_()

        result = self.gamma * ((x - mean) / std)
        
        return result


class BNorm1d(nn.Module):
    def __init__(self, emb):
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(emb))
        self.detach = False
        self.register_buffer('run_var', torch.ones(emb))

    def forward(self, x):
        if self.training:

            var = x.var(dim=(0, 1), unbiased=False, keepdim=True)
            
            if self.detach:
                var = var.detach()

            self.run_var = 0.1 * var.detach().flatten() + 0.9 * self.run_var

        else:
            var = self.run_var

        std = (var + 1e-5).sqrt()

        result = self.gamma * (x / std)
        
        return result
    


class BNorm2d(nn.Module):
    def __init__(self, emb):
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(emb, 1, 1))
        self.detach = False
        self.register_buffer('run_var', torch.ones(emb, 1, 1))

    def forward(self, x):
        if self.training:

            var = x.var(dim=(0, 2, 3), unbiased=False, keepdim=True)
            
            if self.detach:
                var = var.detach()

            self.run_var = 0.1 * var.detach().flatten(0, 1) + 0.9 * self.run_var

        else:
            var = self.run_var

        std = (var + 1e-5).sqrt()

        result = self.gamma * (x / std)
        
        return result
