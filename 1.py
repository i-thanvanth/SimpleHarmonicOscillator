import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.widgets import Slider
try:
    import seaborn as sns
except: print('Seaborn not installed')
else:
    import seaborn as sns
    sns.set()

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)
plt.autoscale(enable=True, axis='y')
fig.canvas.manager.set_window_title('SHO')

#a harmonic oscillator is a system that, when displaced from its equilibrium position, experiences a restoring force F proportional to the displacement x

#set t to be 1000 linearly spaced values from t=0s to 15s
t=np.linspace(0,30,2000)

#a=-ω²x -> -kx=-mω²x -> ω²=k/m
mass=1
springconst=1
omegasq=springconst/mass

#initial position and velocity 
initxandv=[1,0]

#initial damping coefficient
c=0
dc=c/mass

"""

line is a vector that had x and v

line = (x)
       (v)

d(line)   (v)     (v)
------- = --- = ------
dt        (a)   (-ω²x)
"""
#using f=ma for undamped, ma+mω²x = 0 -> d²x/dt² + ω²x = 0 

#for damped oscillations, the frictional force or the resistive force is defined in terms of the velocity of the mass connected to the spring.
#using f=ma for damped, ma+mω²x+cv= 0 -> d²x/dt² + ω²x + c/m dx/dt= 0 

#returns the velocity and the acceleration at time t
def solve_ode(t,y):
    return [y[1],-(dc)*y[1]-omegasq*y[0]]

#solving for position and velocity using initial value ODE solver from SCIpy
output=solve_ivp(solve_ode, [0,2000],y0=initxandv, t_eval=t)
plt.title("""SHO
d²x/dx² + dc*dx/dt + ω² x = 0""") 

"""
plotting the curve with initial values of 
x=1m
v=0m/s
k=1N/m
mass=1kg
dampening coefficient, c=0
"""
line,= plt.plot(t,output.y[0])

#plotting the axes for spring const, mass, velocity, position and the dampening coefficient sliders
axsc = plt.axes([0.275, 0.2, 0.625, 0.03])
axmass = plt.axes([0.275, 0.15, 0.625, 0.03])
axvel = plt.axes([0.275, 0.1, 0.625, 0.03])
axpos = plt.axes([0.275, 0.25, 0.625, 0.03])
axdampingcoefficient = plt.axes([0.275, 0.05, 0.625, 0.03])

#the sliders
mass = Slider(axmass, 'mass - m', 0.0, 10, 2) 
springconst = Slider(axsc, 'spring constant - k', 0.0, 50, 10)
damping = Slider(axdampingcoefficient, u'Damping coeff', 0.0,1,0)
initv = Slider(axvel, 'initial velocity - v', -20,20,0)
initx = Slider(axpos, 'initial position - x', -20,20,1)


#updating the curve whenever the values are changed using sliders
def update(val):
            global omegasq,dc
            m = mass.val
            s = springconst.val
            d=damping.val
            dc= d/m
            x=initx.val
            v=initv.val
            fig.canvas.draw()
            omegasq=s/m
            output=solve_ivp(solve_ode, [0,1000],y0=[x,v], t_eval=t)
            ax.set_ylim([-(abs(v)+abs(x)+5), (abs(v)+abs(x)+5)])
            line.set_ydata(output.y[0])
            fig.canvas.draw_idle()

damping.on_changed(update)
mass.on_changed(update)
springconst.on_changed(update)
initv.on_changed(update)
initx.on_changed(update)

plt.show()