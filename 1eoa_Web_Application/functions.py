import librosa
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import scipy.signal as signal
import librosa
from scipy.fftpack import fft, ifft
import soundfile as sf
import os
import glob
import time

INT16_FAC = (2**15)-1
INT32_FAC = (2**31)-1
INT64_FAC = (2**63)-1
norm_fact = {'int16':INT16_FAC, 'int32':INT32_FAC, 'int64':INT64_FAC,'float32':1.0,'float64':1.0}

def metronome(bpm,timsig,s=[]):
	fs = 44100
	bar = 4
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
	chk = 0
	for i in s:
		if i == 1:
			chk = chk+1

	for counter in range(len(x)):
		if (counter%samplehop==0):
			imp = signal.unit_impulse((int(fs*((60/bpm)*bar*timsig))), [counter])

			if(chk==timsig):
				if (s[si]==1):
					if(countsig==timsig):
						x = x+imp
	                
					else:
						x = x+0.3*imp
				elif (s[si]==0):
					x = x
			else:

				if (s[si]==1):
					if(countsig==timsig):
						x = x+imp
	                
					else:
						x = x+imp
				elif (s[si]==0):
					x = x
	           # if all ones add accents.

	                 
	            
	                
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
	sample_sound = 'static/Data/SampleSounds/Hi Hat 8.wav'
	y, s = librosa.load(sample_sound, sr=fs)
	zeros = np.zeros(x.size-y.size)
	y = np.append(y,zeros)
	Y = fft(y)
	X = fft(x)
	kick1 = np.real(ifft(X*Y))
	#path = "../static/Data/Users/" + user + "/GenSounds/" + "Pulsegen.wav"
	#sf.write("static/Data/GenSounds/Pulsegen.wav", kick1, 44100, 'PCM_24')  
	#write('static/Data/GenSounds/Pulsegen.wav', fs, kick1.astype(np.int16))                  
	return kick1,onset_gen[0],fs
def audiowrite(x, fs, name,pattern):
	path = "static/Data/Users/"+name+"/GenSounds/Pulsegen"+pattern+".wav"
	sf.write(path, x, fs, 'PCM_24') 
	return path


def errordet(audio,fs,onset_gen,s=[]):
	bar = 4
	y,sr = librosa.load(audio, sr = fs)
	y = np.where(y<0.250*np.max(y),0,y)
	onset_frames = librosa.onset.onset_detect(y, sr=sr, hop_length=128, units='samples')
	inter_onset1 = np.zeros(onset_gen.size-1)
	inter_onset2 = np.zeros(onset_frames.size-1)

	for i  in range(inter_onset1.size):     
		inter_onset1[i] =int(onset_gen[i+1])-int(onset_gen[i])
	for i  in range(inter_onset2.size):     
		inter_onset2[i] =int(onset_frames[i+1])-int(onset_frames[i])
	cnt = np.count_nonzero(s)
	#check if both are same sizes print out and error catch it and send it to the html
	if ((inter_onset2.size)<(inter_onset1.size)):
		inter_onset2 = np.tile(inter_onset2,inter_onset1.size)
	
	perc = np.ndarray(shape= (bar,cnt))
	j = 0
	for i in range(bar-1):
		for k in range(cnt):
			perc[i,k] = (inter_onset1[j]-inter_onset2[j])
			perc[i,k] = (perc[i,k]/(inter_onset2[j]))*100
			j+=1
	print(perc)
	cnt = np.count_nonzero(s)
	print(cnt)
	averagebeat = np.zeros(cnt)
	print(averagebeat)
	averagecycle = np.zeros(bar)
	print(averagecycle)

	averagecycle = np.sum(perc,axis =1)
	averagebeat = np.sum(perc,axis=0)
	averagebeat = averagebeat/bar
	averagecycle = averagecycle/cnt
	cnrt = 1
	for i in averagebeat:
		if (float(i)>10):
			cnrt = 0
			break
		elif (float(i)<-10):
			cnrt = 0
			break
		else:
			cnrt = 1
			continue
	
	return averagebeat, averagecycle,cnrt
def plotter(averagebeat,averagecycle,name,s=[]):
	plt.figure()
	plt.subplot(121)
	beats = np.arange(1, averagebeat.size+1)
	cycles = np.arange(1,averagecycle.size+1)
	title0 = 'Error at Each Beat'
	plt.title(title0)
	plt.ylabel('Average Percentage Error')
	plt.xlabel('Beat Interval')
	plt.ylim([-100,100])
	plt.xticks(beats)
	plt.xlim(0.5,averagebeat.size+0.5)
	plt.plot(beats,averagebeat)
	plt.plot(beats,averagebeat,'rx')
	plt.subplot(122)
	title1 = 'Error Across The Cycles'
	plt.title(title1)
	plt.xlabel('Cycle Repeat Number')
	plt.ylim([-100,100])
	plt.xticks(cycles)
	plt.xlim(0.5,averagecycle.size+0.5)
	plt.plot(cycles,averagecycle)
	plt.plot(cycles,averagecycle,'rx')
	plt.suptitle('PATTERN: ' + str(s[0]), fontweight ="bold")
	s = s[0]
	path = "static/Data/Users/"+name+"/results/errorplot"+str(s)+">time:"+str(time.time())+".png"
	plt.savefig(path)  
	return path
def filemanager(name,pat):
	path = "static/Data/Users/"+name+"/results/"
	patternfile = "errorplot"+pat+">"
	l = []
	files = os.listdir(path) 
	for i in files: 
         if patternfile in i: 
             start = i.find(':') 
             stop = i.find('.png') 
             subs = i[start:stop] 
             l.append(subs[1:]) 
	if len(l)==1:
		return 0
	else:
		l.sort(reverse = True)
		k = 1
		while (k < len(l)):
			fullp = path+patternfile+"time:"+l[k]+'.png'
			os.remove(fullp)
			k=k+1
	return 0

			








