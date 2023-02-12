import numpy as np
import matplotlib.pyplot as plt

#deklaracja danych
x1 = np.linspace(0.0,5)
y1 = np.cos(2*np.pi*x1)*np.exp(-x1)

x2 = np.linspace(0.0,2)
y2 = np.cos(2*np.pi*x2)

fig,(ax1,ax2) = plt.subplots(2,1)
fig.suptitle('dwa wykresy: drgania tłumione i nietłumione')

ax1.plot(x1,y1,'o-')
ax1.set_ylabel('aplituda drgań tłumionych')

ax2.plot(x2,y2,'.-')
ax2.set_ylabel('aplituda drgań nietłumionych')
ax2.set_xlabel('czas [s]')

plt.show()
