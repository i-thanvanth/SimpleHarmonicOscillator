import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
amplitude = 2
omega=1 #angular frequency
dc=0.05 #dampening coefficient 
phase = 0 # use np.deg2rad(theta) for other angles
'''
x=[i for i in range(360)]
y=[amplitude*np.cos(np.deg2rad(i)+phase) for i in x]
plt.plot(x,y)
plt.show()
'''
#declaring the figure and the axes and setting the x and y limits for the axes.
fig,axes=plt.figure(),plt.axes(xlim=(0,2),ylim=(-(amplitude+1),(amplitude+1)))
#initiating the line object
line, = axes.plot([],[])
plt.xticks([])
plt.xlabel('time (t)')
plt.ylabel('position of the oscillator w.r.t equilibrium -> x(t)')
x=np.linspace(0,2,1000)
def init():line.set_data([],[]);return line,
def animate(i):
    #x(t)=Acos((ang.freq)*t+phase)
    #2pi(x-0.01*i) updates the values for the cosine wave depending on the frame number
    #y=amplitude*np.cos((2*np.pi*(x-0.01*i))+phase)
    y=amplitude*np.cos(((omega*(x*0.1*i))+phase))*np.exp((-dc)*(x*0.1*i))
    line.set_data(x,y)
    return line,
anim = animation.FuncAnimation(fig,animate,init_func=init,frames=270, interval=20, blit=True)
anim.save('2.mp4',fps=30)
