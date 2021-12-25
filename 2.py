import numpy as np
import matplotlib.pyplot as plt
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
#set t 
t=np.linspace(0,30,5000)

#equation for oscillator without damping
#x=Acos(ωt+φ) -> v=-Aωsin(ωt+φ) -> a=-Aω²cos(ωt+φ) = -ω²x

#equation for oscillator with damping
#x=Ae⁻ᵈᵗcos(ωt+φ)


plt.title(u"""Simple Harmonic Oscillator
x(t)=Ae\u207B\u1d48\u1D57cos(\u03C9t+\u03C6)""",fontname = 'calibri')
phase=np.deg2rad(0)
amplitude=1
omega=1
x=[amplitude*np.cos((omega*i)+phase) for i in t]
line,=plt.plot(t,x)
axfreq = plt.axes([0.275, 0.15, 0.625, 0.03])
axamplitude = plt.axes([0.275, 0.2, 0.625, 0.03])
axdampingcoefficient = plt.axes([0.275, 0.05, 0.625, 0.03])
axphase = plt.axes([0.275, 0.1, 0.625, 0.03])
 
omega = Slider(axfreq, 'Frequency - \u03C9(rad/s)', 0.0, 20.0, 1)
 
amplitude = Slider(axamplitude, 'Amplitude - a (m)', 0.0, 10.0, 1)

damping = Slider(axdampingcoefficient, u'Damping coeff - d', 0.0,1,0)

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

