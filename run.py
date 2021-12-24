import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.widgets import Slider
sns.set()

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)
plt.autoscale(enable=True, axis='y')
fig.canvas.manager.set_window_title('SHO')
#set t 
t=np.linspace(0,30,5000)

#F=ma -> newton's second law
#F=m*d^2(x)/dt^2 
#F= -kx -> restoring force
#x=Acos(ωt+φ) -> v=-Aωsin(ωt+φ) -> a=-Aω^2cos(ωt+φ)
#a=-x*ω^2

#angular_frequency 
plt.title(u"""Simple Harmonic Oscillator
x(t)=Acos(\u03C9t+\u03C6)e\u207B\u1d48\u1D57""",fontname = 'calibri')
phase=np.deg2rad(0)
amplitude=1
omega=1
x=[amplitude*np.cos((omega*i)+phase) for i in t]
line,=plt.plot(t,x)
axfreq = plt.axes([0.3, 0.1, 0.65, 0.03])
axamplitude = plt.axes([0.3, 0.2, 0.65, 0.03])
axdampingcoefficient = plt.axes([0.3, 0.05, 0.65, 0.03])
axphase = plt.axes([0.3, 0.15, 0.65, 0.03])
 
omega = Slider(axfreq, 'Frequency - \u03C9(rad/s)', 0.0, 20.0, 1)
 
amplitude = Slider(axamplitude, 'Amplitude - a (m)', 0.0, 10.0, 1)

damping = Slider(axdampingcoefficient, u'Damping coefficient - d', 0.0,1,0)

phase = Slider(axphase, 'phase - \u03C6 (deg)', 0.0,90,0)

def update(val):
            f = omega.val
            a = amplitude.val
            d=damping.val
            p=phase.val
            value=a*np.exp((-d)*t)*np.cos((f*t)+p)
            line.set_ydata(value)
            fig.canvas.draw()
            ax.set_ylim([-(a+0.5), (a+0.5)])
            fig.canvas.draw_idle()

omega.on_changed(update)
amplitude.on_changed(update)
damping.on_changed(update)
phase.on_changed(update)

plt.show()

