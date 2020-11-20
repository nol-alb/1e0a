# User Input


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


```python
audio = '/Users/noelalben/Desktop/Rythm Recordings/Permutations of 4/1101/Bell Sound/80_bpm.wav'

y,sr = librosa.load(audio, sr = 44100)
y = np.float32(y)/norm_fact[y.dtype.name]
plt.plot(y)
plt.xlabel("Duration in samples")
plt.ylabel("Amplitude")
```




    Text(0, 0.5, 'Amplitude')




![png](output_2_1.png)


## Rectification


```python
y1 = np.where(y<0.10*np.max(y),0,y)
plt.plot(y1)
plt.xlabel("Duration in samples")
plt.ylabel("Amplitude")

```




    Text(0, 0.5, 'Amplitude')




![png](output_4_1.png)



```python

```
