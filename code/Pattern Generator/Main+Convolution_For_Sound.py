if __name__ == "__main__":
    fs = 44100


#Generator Main
    bpm= 140
    timsig = 4
    bar = 6
    s = np.array([1,1,1,0])
    sample_sound = '/Users/noelalben/Downloads/judd-madden-drum-samples/Hi Hat/Hi Hat 8.wav'
    #for i in range(timsig):
     #   n = int(input())
        #if (n==1 or n==0):
         #  s[i] = n
    
    x, onset_gen,fs = metronome(bpm,fs,timsig,bar,s)
    y, s = librosa.load(sample_sound, sr=fs)
    y = np.float32(y)/norm_fact[y.dtype.name]
    zeros = np.zeros(x.size-y.size)
    y = np.append(y,zeros)
    Y = fft(y)
    X = fft(x)

    kick1 = np.real(ifft(X*Y))
    #print(x.size)
    #print(kick1.size)
    write('metHUUBOO.wav', fs, kick1)
    #print(onset_gen)

#Receiver Main
    audio = '/Users/noelalben/Desktop/Rythm Recordings/Hitting Objects/280BPM.wav'
    onset_rec = onset(audio,fs)
    inter_onset1, inter_onset2 = InterOnset(onset_gen,onset_rec)
    per = errorper(inter_onset1, inter_onset2,bar,s)
    per = per*100


