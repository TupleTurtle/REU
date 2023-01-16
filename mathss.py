import numpy as np
import matplotlib.pyplot as plt

def numerical_derivative_1d(func,epsilon):

    def deriv_func(x):

        return (func(x+epsilon)-func(x))/epsilon

    return deriv_func

def f(x):
    return x**2



def grad_descent_v1(f,deriv,x0=None,lr=0.5,iters=400,callback=None):
    
    if x0 is None:
        x0 = np.random.randint(10)

    if callback is not None:
        callback(x0,f(x0))

    derivative=deriv(x0)

    if abs(derivative)<0.000001 or iters==0:
        return x0

    x=x0-derivative*lr

    iters=iters-1

    if abs(deriv(x))>abs(derivative):
        lr=lr/2
        x=x0-derivative*lr

    return grad_descent_v1(f,deriv,x,lr,iters)


print(grad_descent_v1(lambda x: np.log((x + 1)**2 + 1), lambda x: 2 * (x + 1) / (x**2 +1), 1))
