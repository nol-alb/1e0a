import sys, os
sys.path.append('/Users/noelalben/Desktop/Proj2020/Main Proj File Codes')
import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import scipy.signal as signal
import librosa
from scipy.fftpack import fft, ifft
import All_func as pro

INT16_FAC = (2**15)-1
INT32_FAC = (2**31)-1
INT64_FAC = (2**63)-1
norm_fact = {'int16':INT16_FAC, 'int32':INT32_FAC, 'int64':INT64_FAC,'float32':1.0,'float64':1.0}

#Constants
tempos = [145,120,240,227,290]
tempos2 = [145,120,240,227,290]
tempos3 = [120,160,200,240,280]
files = ["/Users/noelalben/Desktop/Rythm Recordings/WritingSample/UserPlay/120_bpm.wav",
         "/Users/noelalben/Desktop/Rythm Recordings/WritingSample/UserPlay/160_bpm.wav",
         "/Users/noelalben/Desktop/Rythm Recordings/WritingSample/UserPlay/200_bpm.wav",
         "/Users/noelalben/Desktop/Rythm Recordings/WritingSample/UserPlay/240_bpm.wav",
         "/Users/noelalben/Desktop/Rythm Recordings/WritingSample/UserPlay/280_bpm.wav"]
array = [1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0]
timsig = 16
cnt = np.count_nonzero(array)
bars = 5

#Computer Generated Beats
x = list() 
onset_gen = list()
for i in range(len(tempos)): 
    j, onset, fs = pro.metronome(tempos[i],44100,timsig,bars,array) 
    x.append(j) 
    onset_gen.append(onset)


#User Inputs
onset_rec = list()
for i in range(len(files)):
                onset1 = pro.onset(files[i],fs)
                onset_rec.append(onset1)

#InterOnset
inter_onset_rec = list()
inter_onset_gen = list()

for i in range(len(tempos)):
    inter_onset1,inter_onset2 = pro.InterOnset(onset_gen[i],onset_rec[i])
    inter_onset_rec.append(inter_onset2)
    inter_onset_gen.append(inter_onset1)


#Errors
percentage = list()

for i in range(len(tempos)):
    perc = pro.errorper(inter_onset_gen[i], inter_onset_rec[i],bars,array)
    percentage.append(perc)


#Averaging it out
averagebeat = list()
averagecycle = list()
for i in range(len(tempos)):
    avgb,avgc = pro.average2(bars,percentage[i],array)
    averagebeat.append(avgb)
    averagecycle.append(avgc)

'''#Plotting
averagecycle1 = np.array(averagecycle)
averagecycle1 = np.transpose(averagecycle1)

averagebeat1 = np.array(averagebeat)
averagebeat1 = np.transpose(averagebeat1)


labels = ['onset interval1']
for i in range(2,cnt+1):
    labels.append('onset interval'+str(i))

labels2 = ['cycle1']
for k in range(2,bars+1):
    labels2.append('cycles'+str(k))

plt.subplot(221)
plt.title('Each Beat')
plt.xlabel('BPM at intervals of 40')
plt.ylabel('Average Perc Error')
plt.ylim([-100,100])
#plt.ylim(-40,40)
for i in range(cnt):  
    plt.plot([80,120,160,200,240],averagecycle1[i],'ro')
    plt.plot([80,120,160,200,240],averagecycle1[i], label = labels[i])
plt.axhline(y=0,xmin = 0, xmax = 300, linewidth = 2, color = 'k')
plt.legend()

plt.subplot(222)
plt.title('Across the cycles')
plt.xlabel('BPM at intervals of 40')
plt.ylabel('Average Perc Error')
plt.ylim([-100,100])
#plt.ylim(-40,40)
for i in range(bars-1):  
    plt.plot([80,120,160,200,240],averagebeat1[i],'ro')
    plt.plot([80,120,160,200,240],averagebeat1[i], label = labels2[i])
plt.axhline(y=0,xmin = 0, xmax = 300, linewidth = 2, color = 'k')
plt.legend()'''

#for wrong
x2 = list() 
onset_gen2 = list()
for i in range(len(tempos2)): 
    j, onset, fs = pro.metronome(tempos2[i],44100,timsig,bars,array) 
    x2.append(j) 
    onset_gen2.append(onset)

    
    
#InterOnset
inter_onset_rec = list()
inter_onset_gen2 = list()

for i in range(len(tempos)):
    inter_onset1,inter_onset2 = pro.InterOnset(onset_gen2[i],onset_rec[i])
    inter_onset_rec.append(inter_onset2)
    inter_onset_gen2.append(inter_onset1)


#Errors
percentage2 = list()

for i in range(len(tempos)):
    perc = pro.errorper(inter_onset_gen2[i], inter_onset_rec[i],bars,array)
    percentage2.append(perc)


#Averaging it out
averagebeat2 = list()
averagecycle2 = list()
for i in range(len(tempos)):
    avgb,avgc = pro.average2(bars,percentage2[i],array)
    averagebeat2.append(avgb)
    averagecycle2.append(avgc)


#Plotting
averagecycle11 = np.array(averagecycle2)
averagecycle11 = np.transpose(averagecycle11)

averagebeat11 = np.array(averagebeat2)
averagebeat11 = np.transpose(averagebeat11)
labels = ['Onset Interval 1']
for i in range(2,cnt+1):
    labels.append('Onset Interval '+str(i))

labels2 = ['Cycle 1']
for k in range(2,bars+1):
    labels2.append('Cycle '+str(k))




plt.figure(1)
#plt.title('Onset Interval Accuracy')
plt.xlabel('BPM at intervals of 40')
plt.ylabel('Average Percentage Error')
plt.ylim([-100,100])
#plt.ylim(-40,40)

for i in range(cnt):  
    plt.plot(tempos3,averagecycle11[i],'ro')
    plt.plot(tempos3,averagecycle11[i],label = labels[i])
#plt.axhline(y=0,xmin = 0, xmax = 300, linewidth = 2, color = 'k')
plt.legend()



plt.figure(2)
#plt.title('Accuracy Across Cycles')
plt.xlabel('BPM at intervals of 40')
plt.ylabel('Average Percentage Error')
plt.ylim([-100,100])

#plt.ylim(-40,40)
for i in range(bars-1):  
    plt.plot(tempos3, averagebeat11[i],'ro')
    plt.plot(tempos3, averagebeat11[i],label = labels2[i])

#plt.axhline(y=0,xmin = 0, xmax = 300, linewidth = 2, color = 'k')
plt.legend()




