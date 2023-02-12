import numpy as np
import matplotlib.pyplot as plt

samplingFrequency = 100
samplingInterval = 1/samplingFrequency

beginTime = 0
endTime =10

signal1Frequency = 4 #4Hz
signal2Frequency = 7 #7Hz

time = np.arange(beginTime,endTime,samplingInterval)

amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
amplitude2 = np.sin(2*np.pi*signal2Frequency*time)

figure, axis = plt.subplots(4,1)
plt.subplots_adjust(hspace=1)

axis[0].set_title('Funkcja falowa o sygnale 4Hz')
axis[0].plot(time,amplitude1)
axis[0].set_xlabel('Czas [s]')
axis[0].set_ylabel('Amplituda')

axis[1].set_title('Funkcja falowa o sygnale 7Hz')
axis[1].plot(time,amplitude2)
axis[1].set_xlabel('Czas [s]')
axis[1].set_ylabel('Amplituda')

#złożenie fukcji falowych
amplitude = amplitude1 + amplitude2


axis[2].set_title('Złożenie dwóch fukcji falowych [4Hz i 7 Hz')
axis[2].plot(time,amplitude)
axis[2].set_xlabel('Czas [s]')
axis[2].set_ylabel('Amplituda')

#transformacja Fouriera dla złożenia fukcji 4 i 7 Hz

fourierTransform = np.fft.fft(amplitude)/len(amplitude)
fourierTransform = fourierTransform[range(int(len(amplitude)/2))]

tpCount = len(amplitude)
values = np.arange(int(tpCount/2))

timePeriod = tpCount/samplingFrequency
frequencies = values/timePeriod

axis[3].set_title('Transformata Fourierawykrślająca składowe czętotliwości')
axis[3].plot(frequencies,abs(fourierTransform))
axis[3].set_xlabel('Częstotliwość')
axis[3].set_ylabel('Amplituda')

plt.show()
