import numpy as np
import matplotlib.pyplot as plt

def numerical_derivative_2d(func,epsilon):
    
    def grad_func(x):

        xDelta = x[0]+epsilon
        zDelta = x[1]+epsilon

        return np.array([func([xDelta,x[1]])/epsilon, func([x[0],zDelta])/epsilon])

    return grad_func

def grad_descent_2d(func, start=None, callback=None, lr=1, iters=80):

    eps = 10**(-10)
    gradient = numerical_derivative_2d(func,eps)

    x0=start
    if x0 is None:
        x0 = np.random.randint(0,2,2)

    if callback is not None:
        callback(x0,func(x0))

    gradientX0=gradient(x0)

    x=x0[0]-gradientX0[0]/(gradientX0[0]-x0[0])*lr
    z=x0[1]-gradientX0[1]/(gradientX0[1]-x0[1])*lr

    altX=x0[0]+gradientX0[0]/(gradientX0[0]-x0[0])*lr
    altZ=x0[1]+gradientX0[1]/(gradientX0[1]-x0[1])*lr

    gradientXZ=gradient([x,z])
    gradientAltXZ=gradient([altX,altZ])

    if gradientXZ[0] < gradientAltXZ[0]:
        bestX=x
    else:
        bestX=altX
    
    if gradientXZ[1] < gradientAltXZ[1]:
        bestZ=z
    else:
        bestZ=altZ

    grad1 = gradient([x0[0],bestZ])
    grad2 = gradient([bestX,x0[1]])

    best=np.array([bestX,bestZ])

    mean = gradient(best)

    if np.sum(grad1)<np.sum(mean):
        x0=[x0[0],bestZ]
    elif np.sum(grad2)<np.sum(mean):
        x0=[bestX,x0[1]]
    elif np.sum(gradientX0)<np.sum(mean):
        pass
    else:
        x0=best

    if abs(np.sum(mean))<0.00001 or iters==0:
        return np.round(x0, 1)

    else:
        lr=lr/2+(80-iters)/10000
        return grad_descent_2d(func,x0,callback,lr,iters-1)



grad_descent_2d(lambda x: (
            -1 / ((x[0] - 1)**2 + (x[1] - 1.5)**2 + 1)
            * np.cos(2 * (x[0] - 1)**2 + 2 * (x[1] - 1.5)**2)
        ),
            np.array([.2 , .7]))