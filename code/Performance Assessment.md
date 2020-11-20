# Performance Assessment


```python
import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import scipy.signal as signal
import librosa
from scipy.fftpack import fft, ifft
INT16_FAC = (2**15)-1
INT32_FAC = (2**31)-1
INT64_FAC = (2**63)-1
norm_fact = {'int16':INT16_FAC, 'int32':INT32_FAC, 'int64':INT64_FAC,'float32':1.0,'float64':1.0}

```

### User Input Onset Detection


```python
audio = '/Users/noelalben/Desktop/Rythm Recordings/Permutations of 4/1101/Hit_Feel/80_bpm.wav'

y,sr = librosa.load(audio, sr = 44100)
y = np.float32(y)/norm_fact[y.dtype.name]
y = np.where(y<0.10*np.max(y),0,y)
plt.plot(y)
plt.xlabel("Duration in samples")
plt.ylabel("Amplitude")



```




    Text(0, 0.5, 'Amplitude')




![png](output_3_1.png)



```python
onset_frames = librosa.onset.onset_detect(y, sr=sr, hop_length=128, units='samples')
plt.vlines(onset_frames, 0, 1, color='r',linestyle='solid', label='Onsets')
```




    <matplotlib.collections.LineCollection at 0x1c2fcd4310>




![png](output_4_1.png)


### Inter Onset Interval User


```python
inter_onset2 = np.zeros(onset_frames.size-1)
```


```python
for i  in range(inter_onset2.size-1):     
        inter_onset2[i] =int(onset_frames[i+1])-int(onset_frames[i])
```


```python
print(inter_onset2)
```

    [33024. 66176. 33152. 33024. 66176. 33024. 33152. 66048. 33152. 33024.
     66176. 33024. 33152. 66176. 33024. 33024. 66176. 33024. 33152. 66176.
     33024. 33024. 66176. 33152. 33024. 66176. 33024. 33152. 66048. 33152.
     33024. 66176. 33024. 33152. 66176. 33024. 33024.     0.]


### Pattern Generator


```python
fs = 44100
bpm= 80
timsig = 4
bar = 8
s = np.array([1,1,0,1])


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
    
onset_gen = np.where(x>0) 
onset_gen = onset_gen[0]

plt.plot(x)
plt.xlabel("Duration in samples")
plt.ylabel("Amplitude")


```




    Text(0, 0.5, 'Amplitude')




![png](output_10_1.png)


### Inter Onset Interval Generated Pattern


```python
inter_onset1 = np.zeros(onset_gen.size-1)
```


```python
for i  in range(inter_onset1.size-1):     
        inter_onset1[i] =int(onset_gen[i+1])-int(onset_gen[i])
```


```python
print(inter_onset1)
```

    [33075. 66150. 33075. 33075. 66150. 33075. 33075. 66150. 33075. 33075.
     66150. 33075. 33075. 66150. 33075. 33075. 66150. 33075. 33075. 66150.
     33075. 33075.     0.]


### Percentage Error


```python

s = np.array([1,1,0,1])
cnt = np.count_nonzero(s)
perc = np.ndarray(shape= (bar,cnt))
j = 0
for i in range(bar-1):
    for k in range(cnt):
            perc[i,k] = (inter_onset1[j]-inter_onset2[j])
            perc[i,k] = (perc[i,k]/(inter_onset2[j]))*100
            j+=1
print(perc)
```

    [[ 1.54433140e-001 -3.92891683e-002 -2.32263514e-001]
     [ 1.54433140e-001 -3.92891683e-002  1.54433140e-001]
     [-2.32263514e-001  1.54433140e-001 -2.32263514e-001]
     [ 1.54433140e-001 -3.92891683e-002  1.54433140e-001]
     [-2.32263514e-001 -3.92891683e-002  1.54433140e-001]
     [ 1.54433140e-001 -3.92891683e-002  1.54433140e-001]
     [-2.32263514e-001 -3.92891683e-002  1.54433140e-001]
     [ 4.57554195e-318  4.73895416e-318  5.06577858e-318]]



```python
average = np.zeros(cnt)
for k in range (cnt):
    for i in range(bar-1):
        average[k] += perc[i,k]
print(average/4)
```

    [-0.0197645  -0.02032547  0.07690967]



```python
plt.plot(np.arange(1,cnt+1),average,'ro')
plt.plot(np.arange(1,cnt+1),average)
plt.xlabel("Onset Interval")
plt.ylabel("Deviation degree")


```




    Text(0, 0.5, 'Deviation degree')




![png](output_18_1.png)



```python

```
