import numpy as np
from compute_function import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#生成网格
#x = [-1,1]
#dt，dx
#the ith element is x[i-1] to x[i+1] means that
#u_{i-1/2} coincide x[i-1] and u_{i+1/2} coincide x[i+1] 
def generate_grid(left,right,dx,T,dt):
    x = np.arange(left,right+dx,dx)
    T = np.arange(0,T+dt,dt)
    return x,T

#初始化
def initial(initial_fun,x):
    u = np.array([0]*len(x))
    for i in range(len(x)):
        u[i] = initial_fun(x[i],-1,1)
    return u

#初始化函数
def initial_fun(x,u_l,u_r):
    if x<0:
        return u_l
    elif x == 0:
        return 0
    else:
        return u_r

def plot_3d(x,t,u):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(x,t,u)
    plt.show()

def plot_2d(x,u):
    plt.plot(x,u)
    plt.show()

#compute_fun是求解格式
def main(left,right,dx,dt,T,initial_fun,compute_fun):
    (x,t) = generate_grid(left,right,dx,T,dt)
    u = initial(initial_fun,x)
    nt = int(T//dt) + 1
    for i in range(nt):
        ut = u
        u = compute_fun(dx,dt,u)
    plot_2d(x,u)

if __name__ == "__main__":
    left = -1
    right = 1
    dx = 0.005
    dt = 0.025
    T = 0.25
    main(left,right,dx,dt,T,initial_fun,lax)