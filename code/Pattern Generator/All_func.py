 #all functions

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


# Function to generate beats
def metronome(bpm, fs,timsig,bar,s=[]):
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
    return x, onset_gen[0],fs

def onset(audio,fs):
    
    y,sr = librosa.load(audio, sr = fs)
    y = np.where(y<0.10*np.max(y),0,y)
    onset_frames = librosa.onset.onset_detect(y, sr=sr, hop_length=128, units='samples')
    
   
    return onset_frames

def InterOnset(onset_gen=[], onset_frames=[]):
    
    inter_onset1 = np.zeros(onset_gen.size-1)
    inter_onset2 = np.zeros(onset_frames.size-1)

    for i  in range(inter_onset1.size):     
        inter_onset1[i] =int(onset_gen[i+1])-int(onset_gen[i])

    for i  in range(inter_onset2.size):     
        inter_onset2[i] =int(onset_frames[i+1])-int(onset_frames[i])

    return inter_onset1, inter_onset2

def errorper (inter_onset1,inter_onset2,bar,s=[]):
    cnt = np.count_nonzero(s)
    perc = np.ndarray(shape= (bar,cnt))
    j = 0
    for i in range(bar-1):
        for k in range(cnt):
            perc[i,k] = (inter_onset1[j]-inter_onset2[j])
            perc[i,k] = (perc[i,k]/(inter_onset2[j]))*100
            j+=1
    return perc

def average2 (bar,perc=[],s=[]):
    cnt = np.count_nonzero(s)
    averagebeat = np.zeros(bar)
    averagecycle = np.zeros(cnt)
    for i in range (cnt):
       for k in range(bar):
            averagebeat[k] += perc[k,i]

    for i in range(bar):
       for k in range(cnt):
            averagecycle[k] += perc[i,k]

    averagebeat = averagebeat/cnt
    averagecycle = averagecycle/bar

    return averagebeat,averagecycle
    
    "{{ songout }}"
    

