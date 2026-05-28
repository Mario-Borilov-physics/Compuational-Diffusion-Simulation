import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as FA
Lx=5
Ly=5
Nx=250
Ny=250
x=np.linspace(0,Lx)
y=np.linspace(0,Ly)
dx=Lx/(Nx-1)
dy=Ly/(Ny-1)
X, Y=np.meshgrid(x,y)
k=0.09
dt=0.001
C_initial=540*np.exp(-((X-Lx/2)**2+(Y-Ly/2)**2)/2)
C=C_initial
fig,ax=plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')

im=ax.pcolormesh(X,Y,C,cmap='plasma',shading='auto',vmin=None,vmax=None)
plt.colorbar(im,label='концентрация C=C(x,y,t)')

def update(frame):
    global C
    C_new=C.copy()
    C_new[1:-1,1:-1]=C[1:-1,1:-1]+k*dt/(dx**2)*(C[2:,1:-1]-2*C[1:-1,1:-1]+C[:-2,1:-1])+k*dt/(dy**2)*(C[1:-1,:-2]-2*C[1:-1,1:-1]+C[1:-1,2:])
    C=C_new
    im.set_array(C.ravel())
    ax.set_title(f't={frame*dt:.2f}')
    return [im]
ani=FA(fig,update,frames=800,interval=2,blit=False,repeat=False)
plt.show()
