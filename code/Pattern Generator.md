# Pattern Generator


```python
INT16_FAC = (2**15)-1
INT32_FAC = (2**31)-1
INT64_FAC = (2**63)-1
norm_fact = {'int16':INT16_FAC, 'int32':INT32_FAC, 'int64':INT64_FAC,'float32':1.0,'float64':1.0}

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import scipy.signal as signal
import librosa
from scipy.fftpack import fft, ifft
```

 ### Pulse Generator


```python
fs = 44100
bpm= 120
timsig = 7
bar = 7
s = np.array([1,1,1,1,0,0,1])
while True:
        if (60*fs%bpm != 0):
            fs+=1
        else:
            break

samplehop= int((60/bpm)*fs)
x = np.zeros(int(fs*((60/bpm)*bar*timsig)))
barc=0
countsig=timsig
si=0
for counter in range(len(x)):
        if (counter%samplehop==0):
             imp = signal.unit_impulse((int(fs*((60/bpm)*bar*timsig))), [counter])
             if (s[si]==1):
                if(countsig==timsig):
                    x = x+imp
                
                else:
                    x = x+ (0.316*imp)
             elif (s[si]==0):
                  x = x
            
                 
            
                
             counter+=1
             countsig-=1
             si+=1
             if(countsig==0):
                countsig = timsig
                barc+=1
                si=0
                if(barc==bar):
                    break

plt.plot(x)
plt.xlabel("Duration in samples")
plt.ylabel("Amplitude")


```




    Text(0, 0.5, 'Amplitude')




![png](output_3_1.png)


### Convolution Function


```python
y, s = librosa.load('/Users/noelalben/Downloads/judd-madden-drum-samples/Hi Hat/Hi Hat 8.wav', sr=fs)
y = np.float32(y)/norm_fact[y.dtype.name]
zeros = np.zeros(x.size-y.size)
y = np.append(y,zeros)
Y = fft(y)
X = fft(x)

kick1 = np.real(ifft(X*Y))
plt.plot(kick1)
plt.xlabel("Duration in samples")
plt.ylabel("Amplitude")
```




    Text(0, 0.5, 'Amplitude')




![png](output_5_1.png)



```python

```
