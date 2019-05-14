import numpy as np

def lax(dx,dt,u):
    #没有处理边界
    new = np.array([0]*len(u))
    for i in range(1,len(u[1:])):
        new[i] = (u[i-1] + u[i+1])/2 - (u[i+1] - u[i-1])*dt/2*dx
    new[0] = -1
    new[-1] = 1
    return new

def LeapFrog(dx,dt,u):
    new = np.array([0]*len(u))
    for i in range(1,len(u[1:])):
        new[i] = u[i] + dt*(u[i+1]-u[i-1])/dx
    return new

def lax_webdroff(dx,dt,u):
    new = np.array([0]*len(u))
    for i in range(1,len(u[1:])):
        new[i] = u[i] - dt*(u[i+1]-u[i-1])/2*dx + dt*dt*(u[i+1]-2*u[i]+u[i-1])/2*dx*dx
    return new