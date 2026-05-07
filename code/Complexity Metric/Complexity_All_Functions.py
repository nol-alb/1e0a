import numpy as np
import math

def cycle_patterns(n):
    bin_arr = range(0, int(math.pow(2,n)))
    bin_arr = [bin(i)[2:] for i in bin_arr]
       
    max_len = len(max(bin_arr, key=len))
    bin_arr = [i.zfill(max_len) for i in bin_arr]
    bin_arr = np.asarray(bin_arr)
    return bin_arr

def cycle_complex_dictionary(bin_arr):
    complexity = {}
    for i in bin_arr:
         complexity[i] = {}
    return complexity

def string_arr_gen(bin_arr,i):
    j = np.asarray(list(bin_arr[i]))
    return j
    
# composite formation
# group adjacent elements until an element TYPE (base char) already in the
# current composite is encountered, then start a new composite.
def code_level_gen_odd_check(j):
    j = list(j)
    k = []
    idx = 0
    while idx < len(j):
        composite_elems = []
        seen_types = set()
        while idx < len(j):
            elem = j[idx]
            elem_type = elem[0]          # base character type: '0' or '1'
            if elem_type in seen_types:
                break
            seen_types.add(elem_type)
            composite_elems.append(elem)
            idx += 1
        k.append(''.join(composite_elems))
    return k



def code_level_gen_odd(j):
    j = list(j)
    k  = []   # composite element strings
    k1 = []   # coded composite strings (letters from code dict)

    code = {}
    for i in range(97, 123):
        code[str(chr(i))] = ''

    elem_to_letter = {}   # element string -> assigned letter (1-to-1 mapping)
    m = 97

    def assign_code(elem):
        nonlocal m
        if elem not in elem_to_letter:
            letter = str(chr(m))
            elem_to_letter[elem] = letter
            code[letter] = elem
            m += 1
        return elem_to_letter[elem]

    idx = 0
    while idx < len(j):
        composite_elems = []
        seen_types = set()
        while idx < len(j):
            elem = j[idx]
            elem_type = elem[0]          # base character type
            if elem_type in seen_types:
                break
            seen_types.add(elem_type)
            composite_elems.append(elem)
            idx += 1

        comp_str    = ''.join(composite_elems)
        comp_coded  = ''.join(assign_code(e) for e in composite_elems)
        k.append(comp_str)
        k1.append(comp_coded)

    # Build statistics
    lensarr = sorted(set(len(c) for c in k1))

    eledic = {}
    for comp in k:
        eledic[comp] = eledic.get(comp, 0) + 1

    lensarrdic = {}
    for comp in eledic:
        lensarrdic[comp] = {l: 0 for l in lensarr}

    lensdic = {l: 0 for l in lensarr}

    for comp_str, comp_coded in zip(k, k1):
        l = len(comp_coded)
        lensarrdic[comp_str][l] += 1   # FIX: was += 2 for singletons
        lensdic[l]              += 1

    return k, lensarr, eledic, lensarrdic, lensdic, k1, code


def get_key(val):
     for key, value in code.items():
          if val == value:
                return key
                
def code_level_gen_even_check(j):
    k1= []
    i=0
    j1 = str()
    while (i < np.size(j)-1):
                    if(j[i]==j[i+1]):
                        for k in range(i,np.size(j)):
                            if(j[i]==j[k]):
                            
                                j1 = j1+j[k]
                                 
                            else:
                                break
                        i = k-1
                        k1.append(j1)
                        j1 = str()
                    else:
                        k1.append(j[i])
                
                    i+=1
                    if(i==np.size(j)-1):
                        if(j[i] != j[i-1]):
                             k1.append(j[i])
    return k1

def code_level_gen_even(j):

    k1= []
    lensdic = {}
    eledic = {}
    lensarr = []
    lensarrdic = {}
    code = {}
    for i in range(97,123):
        code[str(chr(i))] = ''
    for i in j:
        eledic[i] = 0

    k2 = []
    i=0
    j1 = str()
    j2 = str()
    m = 97
    def get_key(val):
      for key, value in code.items():
         if val == value:
               return key
               
               

    while (i < np.size(j)-1):
                if(j[i]==j[i+1]):
                    code[str(chr(m))] = j[i]
                    cnt = 0
                    for k in range(i,np.size(j)):
                        if(j[i]==j[k]):
                            j1 = j1+j[k]
                            j2 = j2 + get_key(j[i])
                            cnt = cnt+1
                        else:
                            if cnt in lensarr:
                               break
                            else:
                                lensarr.append(cnt)
                                break
                    i = k-1
                    k1.append(j1)
                    k2.append(j2)
                    eledic[j[i]] = eledic[j[i]]+1
                    j1 = str()
                    j2 = str()
                    m= m+1
                else:
                    if  (1 in lensarr):
                        k1.append(j[i])
                        code[str(chr(m))] = j[i]
                        ke = get_key(j[i])
                        k2.append(ke)
                        eledic[j[i]] = eledic[j[i]]+1
                        m = m+1
                        
                    else:
                        lensarr.append(1)
                        code[str(chr(m))] = j[i]
                        ke = get_key(j[i])
                        k2.append(ke)
                        k1.append(j[i])
                        eledic[j[i]] = eledic[j[i]]+1
                        m = m+1
                            
                i+=1
                if(i==np.size(j)-1):
                    if(j[i] != j[i-1]):
                        if  (1 in lensarr):
                            k1.append(j[i])
                            code[str(chr(m))] = j[i]
                            ke = get_key(j[i])
                            k2.append(ke)
                            eledic[j[i]] = eledic[j[i]]+1
                            m = m+1
                        else:
                            lensarr.append(1)
                            k1.append(j[i])
                            eledic[j[i]] = eledic[j[i]]+1
                            code[str(chr(m))] = j[i]
                            ke = get_key(j[i])
                            k2.append(ke)
                            m = m+1
    lensarr = []
    for i in k2:
        if len(i) in lensarr:
            continue
        else:
           lensarr.append(len(i))

    lensdic = {}
    for i in j:
        lensdic[i] = {}
    for i in j:
        for k in lensarr:
            lensdic[i][k] = 0
    for i in lensarr:
        lensarrdic[i] = 0
    i=0
    j1 = str()
    while (i < np.size(j)-1):
                if(j[i]==j[i+1]):
                    cnt = 0
                    for k in range(i,np.size(j)):
                        if(j[i]==j[k]):
                            j1 = j1+j[k]
                            cnt = cnt+1
                        else:
                            lensdic[j[i]][cnt] = lensdic[j[i]][cnt] + 1
                            lensarrdic[cnt] = lensarrdic[cnt] + 1
                            break
                    i = k-1
                    j1 = str()
                else:
                        lensarrdic[1] = lensarrdic[1] + 1
                        lensdic[j[i]][1] = lensdic[j[i]][1] + 1
                i+=1
                if(i==np.size(j)-1):
                    if(j[i] != j[i-1]):
                         lensarrdic[1] = lensarrdic[1] + 1
                         lensdic[j[i]][1] = lensdic[j[i]][1] + 1
                         

    return k1, lensdic, eledic,lensarr,lensarrdic,k2,code
    
def lendic(j):
    lensdict = {}
    k=0
    lensarr = []
    for i in j:
      j1 = list(i)
      l = len(j1)
      if l in lensarr:
        continue
      lensarr.append(l)
    for i in lensarr:
       lensdict[i] = 0
    for i in j:
      j1 = list(i)
      l = len(j1)
      lensdict[l] = lensdict[l]+1
    return lensarr , lensdict
    
def eledic(j):
    eledict = {}
    for i in j:
      eledict[i] = 0
    for i in j:
      eledict[i] = eledict[i]+1
    return eledict

def lendic_hjoint(j,lensarr):
    lendicpro ={}
    for i in j:
       lendicpro[i] = {}

    for i in j:
        for k in lensarr:
             lendicpro[i][k] = 0
    for i in j:
     j1 = list(i)
     l = len(j1)
     lendicpro[i][l]=lendicpro[i][l]+1
    return lendicpro


def Hmax_gen(eledict, lensdict, j):
    total_x = sum(eledict.values())
    probx = {}
    for i in eledict:
        probx[i] = eledict[i] / total_x

    Hx=0
    for i in probx:
        if probx[i] > 0:
            Hx = Hx + abs(probx[i] * np.log2(probx[i]))

    total_y = sum(lensdict.values())
    proby = {}
    for i in lensdict:
        proby[i] = lensdict[i] / total_y
    
    Hy = 0
    for i in lensdict:
        if proby[i] == 0:
           continue
        Hy = Hy + abs(proby[i] * np.log2(proby[i]))

    Hmax = 2*Hy + 2*Hx
    return Hmax


def Hx_gen(eledict, j):
    total = sum(eledict.values())
    Hx = 0
    for i in eledict:
        p = eledict[i] / total
        if p > 0:
            Hx += abs(p * np.log2(p))
    return Hx


def All_pairs(j):
    pairs = []
    o = j
    [pairs.append([o[i],o[i+1]]) for i in range(len(o)-1)]
    pairs.append([o[len(o)-1],o[0]])
    return pairs



def Hse_len(eledict, lensdict, lensarr,j):
    j1 = np.asarray(j)

    probxy = {}
    for i in lensdict:
        probxy[i] = {}
        for k in lensarr:
            probxy[i][k] = 0
            probxy[i][k] =lensdict[i][k]/eledict[i]
    probx = {}
    for i in eledict:
     probx[i] = eledict[i]/np.size(j)
    Hxy = 0
    for i in lensdict:
       for k in lensarr:
         if(probxy[i][k]==0):
            continue
         Hxy = abs(Hxy+(probx[i]*np.log2(probxy[i][k])))

    return Hxy, probx, probxy

def combined_probxy(probx, probxy,lensdict, lensarr,eledict):
    cprobxy = {}

    for i in eledict:
      cprobxy[i] = {}

    for i in lensdict:
        for k in lensarr:
             cprobxy[i][k] = 0

    for i in lensdict:
        for k in lensarr:
             cprobxy[i][k] = 0

    for i in lensdict:
       for k in lensarr:
         cprobxy[i][k] = probx[i]*probxy[i][k]
    return cprobxy

def hselen_re(eledict, lensdict, pairs, lensarr, cprobxy, code):
    probxyx={}
    for i in eledict:
       probxyx[i] = {}
    for i in eledict:
        for k in lensarr:
         probxyx[i][k]={}
        
    for i in eledict:
        for k in lensarr:
          for l in eledict:
             probxyx[i][k][l]=0
    
    for l in pairs:
          m = l[0]
          f = len(m)
          if(f == 1):
           m = code[m[0]]
           o = l[1]
           o = code[o[0]]
           
          else:
              m1 = code[m[0]]
              m2 = code[m[1]]
              m = m1+m2
              o = l[1]
              f1 = len(o)
              if(f1 == 1):
                o = code[o[0]]
              else:
                o1 = code[o[0]]
                o2 = code[o[1]]
                o = o1+o2
              probxyx[m][f][o]=probxyx[m][f][o]+1

    for i in eledict:
     for k in lensarr:
              if(lensdict[i][k]==0):
                  continue
              for m in eledict:
                 probxyx[i][k][m]=probxyx[i][k][m]/lensdict[i][k]

    Hxyx = 0
    for i in eledict:
        for k in lensarr:
              for m in eledict:
                if(probxyx[i][k][m]==0):
                  continue
                Hxyx = abs(Hxyx + (cprobxy[i][k]*np.log2(probxyx[i][k][m])))

    return Hxyx, probxyx
    
def hselen_re1(eledict, lensdict, pairs, lensarr, cprobxy):
    probxyx={}
    for i in eledict:
       probxyx[i] = {}
    for i in eledict:
        for k in lensarr:
         probxyx[i][k]={}
        
    for i in eledict:
        for k in lensarr:
          for l in eledict:
             probxyx[i][k][l]=0

    for l in pairs:
          m = l[0]
          f = len(m)
          o = l[1]
          probxyx[m][f][o]=probxyx[m][f][o]+1

    for i in eledict:
     for k in lensarr:
              if(lensdict[i][k]==0):
                  continue
              for m in eledict:
                 probxyx[i][k][m]=probxyx[i][k][m]/lensdict[i][k]

    Hxyx = 0
    for i in eledict:
        for k in lensarr:
              for m in eledict:
                if(probxyx[i][k][m]==0):
                  continue
                Hxyx = abs(Hxyx + (cprobxy[i][k]*np.log2(probxyx[i][k][m])))

    return Hxyx, probxyx

def hselen_re_even(eledict, lensdict, pairs, lensarr, cprobxy,code):
    probxyx={}
    for i in eledict:
       probxyx[i] = {}
    for i in eledict:
        for k in lensarr:
         probxyx[i][k]={}
        
    for i in eledict:
        for k in lensarr:
          for l in eledict:
             probxyx[i][k][l]=0


    for l in pairs:
          m = l[0]
          f = len(m)
          m = code[m[0]]
          o = l[1]
          o = code[o[0]]
          probxyx[m][f][o]=probxyx[m][f][o]+1

 
 
    for i in eledict:
     for k in lensarr:
              if(lensdict[i][k]==0):
                  continue
              for m in eledict:
                 probxyx[i][k][m]=probxyx[i][k][m]/lensdict[i][k]

    Hxyx = 0
    for i in eledict:
        for k in lensarr:
              for m in eledict:
                if(probxyx[i][k][m]==0):
                  continue
                Hxyx = abs(Hxyx + (cprobxy[i][k]*np.log2(probxyx[i][k][m])))

    return Hxyx, probxyx


def combined_probxyx(cprobxy,probxyx,lensdict, lensarr,eledict):
    cprobxyx = {}

    for i in eledict:
     cprobxyx[i] = {}

    for i in lensdict:
        for k in lensarr:
            cprobxyx[i][k] = {}

    for i in lensdict:
        for k in lensarr:
              for m in eledict:
                cprobxyx[i][k][m] = 0

    for i in eledict:
       for k in lensarr:
              for m in eledict:
                  cprobxyx[i][k][m] = (cprobxy[i][k] * probxyx[i][k][m])

    return cprobxyx

def hselenre_len(cprobxyx,eledict, lensdict,pairs, lensarr, code):
    numxyx={}
    for i in eledict:
     numxyx[i] = {}
    for i in eledict:
     for k in lensarr:
      numxyx[i][k]={}

    for i in eledict:
     for k in lensarr:
        for l in eledict:
            numxyx[i][k][l]=0
    for l in pairs:
           m = l[0]
           f = len(m)
           if(f == 1):
            m = code[m[0]]
            o = l[1]
            o = code[o[0]]
            
           else:
               m1 = code[m[0]]
               m2 = code[m[1]]
               m = m1+m2
               o = l[1]
               n = len(o)
               if(n == 1):
                 o = code[o[0]]
               else:
                 o1 = code[o[0]]
                 o2 = code[o[1]]
                 o = o1+o2
               numxyx[m][f][o]=numxyx[m][f][o]+1

    
    probxyxy={}
    for i in eledict:
        probxyxy[i] = {}
    for i in eledict:
        for k in lensarr:
           probxyxy[i][k]={}

    for i in eledict:
        for k in lensarr:
            for l in eledict:
                probxyxy[i][k][l]= {}
    for i in eledict:
        for k in lensarr:
            for l in eledict:
                for m in lensarr:
                  probxyxy[i][k][l][m]= 0
            
            
            
    for i in pairs:
         u = i[0]
         n = len(u)
         if (n==1):
            u = code[u[0]]
            l = i[1]
            p = len(l)
            if(p == 1):
              l = code[l[0]]
            else:
              l1 = code[l[0]]
              l2 = code[l[1]]
              l = l1+l2
            probxyxy[u][n][l][p]= probxyxy[u][n][l][p] + 1
         else:
        
             u1 = code[u[0]]
             u2 = code[u[1]]
             u = u1+u2
             l = i[1]
             p = len(l)
             if(p == 1):
               l = code[l[0]]
             else:
               l1 = code[l[0]]
               l2 = code[l[1]]
               l = l1+l2
             probxyxy[u][n][l][p]= probxyxy[u][n][l][p] + 1


    for i in eledict:
     for k in lensarr:
              for m in eledict:
                  if(numxyx[i][k][m]==0):
                     continue
                  for l in lensarr:
                      probxyxy[i][k][m][l]=probxyxy[i][k][m][l]/numxyx[i][k][m]

    Hxyxy = 0
    for i in eledict:
     for k in lensarr:
              for m in eledict:
                  for l in lensarr:
                     if(probxyxy[i][k][m][l]==0):
                       continue
                     Hxyxy = abs(Hxyxy + (cprobxyx[i][k][m]*np.log2(probxyxy[i][k][m][l])))

    return Hxyxy, probxyxy

def hselenre_len_even(cprobxyx,eledict, lensdict,pairs, lensarr,code):
    numxyx={}
    for i in eledict:
     numxyx[i] = {}
    for i in eledict:
     for k in lensarr:
      numxyx[i][k]={}

    for i in eledict:
     for k in lensarr:
        for l in eledict:
            numxyx[i][k][l]=0
    for l in pairs:
           m = l[0]
           f = len(m)
           m = code[m[0]]
           o = l[1]
           o = code[o[0]]
           numxyx[m][f][o]=numxyx[m][f][o]+1

    
    probxyxy={}
    for i in eledict:
        probxyxy[i] = {}
    for i in eledict:
        for k in lensarr:
           probxyxy[i][k]={}

    for i in eledict:
        for k in lensarr:
            for l in eledict:
                probxyxy[i][k][l]= {}
    for i in eledict:
        for k in lensarr:
            for l in eledict:
                for m in lensarr:
                  probxyxy[i][k][l][m]= 0
            
            
            
    for i in pairs:
         q = i[0]
         n = len(q)
         m = code[q[0]]
         l = i[1]
         p = len(l)
         o = code[l[0]]
         probxyxy[m][n][o][p]= probxyxy[m][n][o][p] + 1


    for i in eledict:
     for k in lensarr:
              for m in eledict:
                  if(numxyx[i][k][m]==0):
                     continue
                  for l in lensarr:
                      probxyxy[i][k][m][l]=probxyxy[i][k][m][l]/numxyx[i][k][m]

    Hxyxy = 0
    for i in eledict:
     for k in lensarr:
              for m in eledict:
                  for l in lensarr:
                     if(probxyxy[i][k][m][l]==0):
                       continue
                     Hxyxy = abs(Hxyxy + (cprobxyx[i][k][m]*np.log2(probxyxy[i][k][m][l])))

    return Hxyxy, probxyxy