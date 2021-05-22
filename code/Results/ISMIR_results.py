import sys, os
sys.path.append('/Users/noelalben/1e0awebapp')
import functions.py as func
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import pandas as pd






def str_int_list(z):
	f = list(str(z)) 
	cnt = 0 
	for o in f: 
		f[cnt]=int(o) 
		cnt=cnt+1
	return f

def patterngen(bpm,cycle,s=[]):
	x,onsetgen, fs = metronome(bpm,cycle,s)
	return x,onsetgen,fs



timsig = ['4','3','5','7']
names = ['Aniket Acharya','Samson Antony', 'aastha','Neithe', 'Harshavardhan','Eva', 'Ajay']
l4 = ['1111','1010','1001','1101','0001','0110'] 
l3 = ['111','110','001','010'] 
l5 = ['11111','10100','10110','11101','11011','10101','01010'] 
l7= ['1111111','1111000','1101100','0100101','0001010','0111010']
l = [l4,l3,l5,l7]

cnt = 0
d41 = [[] for i in range(len(names))]
d42 = [[] for i in range(len(names))]
d43 = [[] for i in range(len(names))]
d44 = [[] for i in range(len(names))]
path0=[]
upb=0
upc=0
for i in names:
    for j in l4:
        path = "/Users/noelalben/1e0awebapp/static/Data/Users/"+i+"/recordings/audio"+j+".wav"
        path0.append(path)
        pattern = str_int_list(j)
        x,onsetgen, fs = patterngen(160,4,pattern)
        averagebeat, averagecycle,n = errordet(path0[0],fs,onsetgen,pattern)
        averagecycle1 = np.sum(abs(averagecycle))/np.size(averagecycle)
        averagecyclesd = np.std(abs(averagecycle))
        averagebeat1 = np.sum(abs(averagebeat))/np.size(averagebeat)
        averagebeatsd = np.std(abs(averagebeat))
        d41[upb].append(averagebeatsd)
        d42[upc].append(averagecyclesd)
        d43[upb].append(averagebeat1)
        d44[upc].append(averagecycle1)
        path0=[]
    upb=upb+1
    upc=upc+1

d51 = [[] for i in range(len(names))]
d52 = [[] for i in range(len(names))]
d53 = [[] for i in range(len(names))]
d54 = [[] for i in range(len(names))]
path0=[]
upb=0
upc=0
for i in names:
    for j in l5:
        path = "/Users/noelalben/1e0awebapp/static/Data/Users/"+i+"/recordings/audio"+j+".wav"
        path0.append(path)
        pattern = str_int_list(j)
        x,onsetgen, fs = patterngen(160,5,pattern)
        averagebeat, averagecycle,n = errordet(path0[0],fs,onsetgen,pattern)
        averagecycle1 = np.sum(abs(averagecycle))/np.size(averagecycle)
        averagecyclesd = np.std(abs(averagecycle))
        averagebeat1 = np.sum(abs(averagebeat))/np.size(averagebeat)
        averagebeatsd = np.std(abs(averagebeat))
        d51[upb].append(averagebeatsd)
        d52[upc].append(averagecyclesd)
        d53[upb].append(averagebeat1)
        d54[upc].append(averagecycle1)
        path0=[]
    upb=upb+1
    upc=upc+1

d31 = [[] for i in range(len(names))]
d32 = [[] for i in range(len(names))]
d33 = [[] for i in range(len(names))]
d34 = [[] for i in range(len(names))]
path0=[]
upb=0
upc=0
for i in names:
    for j in l3:
        path = "/Users/noelalben/1e0awebapp/static/Data/Users/"+i+"/recordings/audio"+j+".wav"
        path0.append(path)
        pattern = str_int_list(j)
        x,onsetgen, fs = patterngen(160,3,pattern)
        averagebeat, averagecycle,n = errordet(path0[0],fs,onsetgen,pattern)
        averagecycle1 = np.sum(abs(averagecycle))/np.size(averagecycle)
        averagecyclesd = np.std(abs(averagecycle))
        averagebeat1 = np.sum(abs(averagebeat))/np.size(averagebeat)
        averagebeatsd = np.std(abs(averagebeat))
        d31[upb].append(averagebeatsd)
        d32[upc].append(averagecyclesd)
        d33[upb].append(averagebeat1)
        d34[upc].append(averagecycle1)
        path0=[]
    upb=upb+1
    upc=upc+1

d71 = [[] for i in range(len(names))]
d72 = [[] for i in range(len(names))]
d73 = [[] for i in range(len(names))]
d74 = [[] for i in range(len(names))]
path0=[]
upb=0
upc=0
for i in names:
    for j in l7:
        path = "/Users/noelalben/1e0awebapp/static/Data/Users/"+i+"/recordings/audio"+j+".wav"
        path0.append(path)
        pattern = str_int_list(j)
        x,onsetgen, fs = patterngen(160,7,pattern)
        averagebeat, averagecycle,n = errordet(path0[0],fs,onsetgen,pattern)
        averagecycle1 = np.sum(abs(averagecycle))/np.size(averagecycle)
        averagecyclesd = np.std(abs(averagecycle))
        averagebeat1 = np.sum(abs(averagebeat))/np.size(averagebeat)
        averagebeatsd = np.std(abs(averagebeat))
        d71[upb].append(averagebeatsd)
        d72[upc].append(averagecyclesd)
        d73[upb].append(averagebeat1)
        d74[upc].append(averagecycle1)
        path0=[]
    upb=upb+1
    upc=upc+1

        # Aniket
        # Anik4listb=[]
        # Anik4listc=[]
        # Nei4listb=[]
        # Sam4listb=[]
        # aast4listb=[]
        # eva4listb=[]
        # ajay4listb = []
        # Nei4listc=[]
        # Sam4listc=[]
        # aast4listc=[]
        # eva4listc=[]
        # Aniksd4listb=[]
        # Aniksd4listc=[]
        # Ajay4listc = []
        # Neisd4listb=[]
        # Samsd4listb=[]
        # aastsd4listb=[]
        # evasd4listb=[]
        # Neisd4listc=[]
        # Samsd4listc=[]
        # aastsd4listc=[]
        # evasd4listc=[]
        # Fulllist4b=[Anik4listb,Nei4listb,Sam4listb,aast4listb,eva4listb]
        # Fulllist4c=[Anik4listc,Nei4listc,Sam4listc,aast4listc,eva4listc]
        # Fulllistsd4b=[Aniksd4listb,Neisd4listb,Samsd4listb,aastsd4listb,evasd4listb]
        # Fulllistsd4c=[Aniksd4listc,Neisd4listc,Samsd4listc,aastsd4listc,evasd4listc]
        # path0=[]
        # upb=0
        # upc=0
        # for i in names:
        #     for j in l4:
        #         path = "/Users/noelalben/1e0awebapp/static/Data/Users/"+i+"/recordings/audio"+j+".wav"
        #         path0.append(path)
        #         pattern = str_int_list(j)
        #         x,onsetgen, fs = patterngen(160,4,pattern)
        #         averagebeat, averagecycle,n = errordet(path0[0],fs,onsetgen,pattern)
        #         averagecycle1 = np.sum(abs(averagecycle))/np.size(averagecycle)
        #         averagecyclesd = np.std(abs(averagecycle))
        #         averagebeat1 = np.sum(abs(averagebeat))/np.size(averagebeat)
        #         averagebeatsd = np.std(abs(averagebeat))
        #         Fulllistsd4b[upb].append(averagebeatsd)
        #         Fulllistsd4c[upc].append(averagecyclesd)
        #         Fulllist4b[upb].append(averagebeat1)
        #         Fulllist4c[upc].append(averagecycle1)
        #         path0=[]
        #     upb=upb+1
        #     upc=upc+1



plt.figure() 
plt.title('Average Absolute Cycle Error')  
plt.xlabel('Patterns of 4')  
plt.ylabel('Average Perc Error')  
plt.ylim([0,10])
k = 0
for i in range(len(names)):
    if (k<3):
        if(k==0):

            lines = plt.errorbar(l4,d43[i],d41[i],marker='o',linestyle='none', label='Amateur',color='orange')
        else:
            lines = plt.errorbar(l4,d43[i],d41[i],marker='o',linestyle='none',color='orange') 
        k = k+1
    elif(3<=k<5):
        if (k==3):

            lines = plt.errorbar(l4,d43[i],d41[i],marker='o',linestyle='none', label='Beginner',color='red')
        else:
            lines = plt.errorbar(l4,d43[i],d41[i],marker='o',linestyle='none',color='red')
        k = k+1
    else:
        if(k==5):

            lines = plt.errorbar(l4,d43[i],d41[i],marker='o',linestyle='none', label='Professional',color='mediumpurple')
        else:
            lines = plt.errorbar(l4,d43[i],d41[i],marker='o',linestyle='none',color='mediumpurple')
        k = k+1
plt.grid()  
plt.legend()  
plt.savefig('ErrorPatterns18')



dlist = [[] for i in range(len(names))]
cnt = 0
for i in names:
    filename='/Users/noelalben/1e0awebapp/static/Data/Users/'+i+'/results/results.csv'
    df=pd.read_csv(filename,dtype={'Pattern':object})
    g = df.groupby('Pattern')['Name'].count()
    for j in l:
        cntr = []
        for k in j:
            value = g[k]
            cntr.append(value)
        dlist[cnt].append(cntr)
    cnt=cnt+1

plt.figure() 
plt.title('Total number of attempts')  
plt.xlabel('Patterns of 7')  
plt.ylabel('No. Of Attempts')  
plt.ylim([0,10])
k = 0
for i in range(len(names)):
    if (i<3):
        if(i==0):
            plt.scatter(l7,dlist[i][3],label = 'Amateur',color='orange') 
        else:
            plt.scatter(l7,dlist[i][3],color='orange') 
    elif(3<=i<5):
        if (i==3):

            plt.scatter(l7,dlist[i][3],label = 'Beginner',color='red') 
        else:
            plt.scatter(l7,dlist[i][3],color='red') 
    else:
        if(i==5):

            plt.scatter(l7,dlist[i][3],label = 'Professional',color='mediumpurple') 
        else:
            plt.scatter(l7,dlist[i][3],color='mediumpurple') 
plt.grid()  
plt.legend()  
plt.savefig('ErrorPatterns121')


# plt.figure() 
# plt.title('Average Absolute Cycle Error') 
# plt.xlabel('Patterns of 4') 
# plt.ylabel('Average Perc Error') 
# plt.ylim([0,10]) 
# for i in range(len(names)):   
# # plt.plot(l7,Fulllist7c[i],'ro')
#     plt.scatter(l4,dlist[i][0],label = legend[i]) 
#     #plt.errorbar(l4,Fulllist4b[i],Fulllistsd4b[i])
      
# plt.grid() 
# plt.legend() 
# plt.savefig('ErrorPatterns20') 




Patterns = ["Patterns of 4", "Patterns of 3", "Patterns of 5", "Patterns of 7"]
Namesc = ["Errorp4cycle","Errorp3cycle","Errorp5cycle","Errorp7cycle"]
Namesb = ["Errorp4beat","Errorp3beat","Errorp5beat","Errorp7beat"]
Namesa = ["Errorp4at","Errorp3at","Errorp5at","Errorp7at"]
cyclesin = [4,3,5,7]
ocyc=0
for cyclenum in l:
    d41 = [[] for i in range(len(names))]
    d42 = [[] for i in range(len(names))]
    d43 = [[] for i in range(len(names))]
    d44 = [[] for i in range(len(names))]
    path0=[]
    upb=0
    upc=0
    for i in names:
        for j in cyclenum:
            path = "/Users/noelalben/1e0awebapp/static/Data/Users/"+i+"/recordings/audio"+j+".wav"
            path0.append(path)
            pattern = str_int_list(j)
            x,onsetgen, fs = patterngen(160,cyclesin[ocyc],pattern)
            averagebeat, averagecycle,n = errordet(path0[0],fs,onsetgen,pattern)
            averagecycle1 = np.sum(abs(averagecycle))/np.size(averagecycle)
            averagecyclesd = np.std(abs(averagecycle))
            averagebeat1 = np.sum(abs(averagebeat))/np.size(averagebeat)
            averagebeatsd = np.std(abs(averagebeat))
            d41[upb].append(averagebeatsd)
            d42[upc].append(averagecyclesd)
            d43[upb].append(averagebeat1)
            d44[upc].append(averagecycle1)
            path0=[]
        upb=upb+1
        upc=upc+1

    plt.figure() 
    plt.title('Average Absolute Cycle Error')  
    plt.xlabel(Patterns[ocyc])  
    plt.ylabel('Average Perc Error')  
    plt.ylim([0,10])
    k = 0
    for i in range(len(names)):
        if (k<3):
            if(k==0):

                lines = plt.errorbar(cyclenum,d44[i],d42[i],marker='x',linestyle='none', label='Amateur',color='orange')
            else:
                lines = plt.errorbar(cyclenum,d44[i],d42[i],marker='x',linestyle='none',color='orange') 
            k = k+1
        elif(3<=k<5):
            if (k==3):

                lines = plt.errorbar(cyclenum,d44[i],d42[i],marker='*',linestyle='none', label='Beginner',color='red')
            else:
                lines = plt.errorbar(cyclenum,d44[i],d42[i],marker='*',linestyle='none',color='red')
            k = k+1
        else:
            if(k==5):

                lines = plt.errorbar(cyclenum,d44[i],d42[i],marker='o',linestyle='none', label='Professional',color='mediumpurple')
            else:
                lines = plt.errorbar(cyclenum,d44[i],d42[i],marker='o',linestyle='none',color='mediumpurple')
            k = k+1
    plt.grid()  
    plt.legend()  
    plt.savefig(Namesc[ocyc])

    plt.figure() 
    plt.title('Average Absolute Beat Error')  
    plt.xlabel(Patterns[ocyc])  
    plt.ylabel('Average Perc Error')  
    plt.ylim([0,10])
    k = 0
    for i in range(len(names)):
        if (k<3):
            if(k==0):

                lines = plt.errorbar(cyclenum,d43[i],d41[i],marker='x',linestyle='none', label='Amateur',color='orange')
            else:
                lines = plt.errorbar(cyclenum,d43[i],d41[i],marker='x',linestyle='none',color='orange') 
            k = k+1
        elif(3<=k<5):
            if (k==3):

                lines = plt.errorbar(cyclenum,d43[i],d41[i],marker='*',linestyle='none', label='Beginner',color='red')
            else:
                lines = plt.errorbar(cyclenum,d43[i],d41[i],marker='*',linestyle='none',color='red')
            k = k+1
        else:
            if(k==5):

                lines = plt.errorbar(cyclenum,d43[i],d41[i],marker='o',linestyle='none', label='Professional',color='mediumpurple')
            else:
                lines = plt.errorbar(cyclenum,d43[i],d41[i],marker='o',linestyle='none',color='mediumpurple')
            k = k+1
    plt.grid()  
    plt.legend()  
    plt.savefig(Namesb[ocyc])



    dlist = [[] for i in range(len(names))]
    cnt = 0
    for i in names:
        filename='/Users/noelalben/1e0awebapp/static/Data/Users/'+i+'/results/results.csv'
        df=pd.read_csv(filename,dtype={'Pattern':object})
        g = df.groupby('Pattern')['Name'].count()
        for j in l:
            cntr = []
            for k in j:
                value = g[k]
                cntr.append(value)
            dlist[cnt].append(cntr)
        cnt=cnt+1

    plt.figure() 
    plt.title('Total number of attempts')  
    plt.xlabel(Patterns[ocyc])  
    plt.ylabel('No. Of Attempts')  
    plt.ylim([0,10])
    k = 0
    for i in range(len(names)):
        if (i<3):
            if(i==0):
                plt.scatter(cyclenum,dlist[i][ocyc],marker='x',label = 'Amateur',color='orange') 
            else:
                plt.scatter(cyclenum,dlist[i][ocyc],marker='x',color='orange') 
        elif(3<=i<5):
            if (i==3):

                plt.scatter(cyclenum,dlist[i][ocyc],marker='*',label = 'Beginner',color='red') 
            else:
                plt.scatter(cyclenum,dlist[i][ocyc],marker='*',color='red') 
        else:
            if(i==5):

                plt.scatter(cyclenum,dlist[i][ocyc],marker='o',label = 'Professional',color='mediumpurple') 
            else:
                plt.scatter(cyclenum,dlist[i][ocyc],marker='o',color='mediumpurple') 
    plt.grid()  
    plt.legend()  
    plt.savefig(Namesa[ocyc])
    ocyc = ocyc+1
