import sys, os
sys.path.append('/Users/noelalben/Desktop/Proj2020/Main Proj File Codes')
import Complexity_All_Functions as CAF
import csv



def complexity_of_cycle(n):

    def complex_level1(bin_arr,c):

        j = CAF.string_arr_gen(bin_arr,c)
        lensarr , lensdict = CAF.lendic(j)
        eledict = CAF.eledic(j)
        Hmax = CAF.Hmax_gen(eledict, lensdict, j)
        lendicpro = CAF.lendic_hjoint(j,lensarr)
        pairs = CAF.All_pairs(j)
        Hxy, probx, probxy = CAF.Hse_len(eledict, lendicpro, lensarr,j)
        cprobxy = CAF.combined_probxy(probx, probxy,lendicpro, lensarr,eledict)
        Hxyx, probxyx = CAF.hselen_re1(eledict, lendicpro, pairs, lensarr, cprobxy)
        Htotal = 0
        Htotal = Hmax+ Hxy+Hxyx
        
        return Htotal,j
        
    def complex_level_even(j):
        je, lensdic, eledic,lensarr,lensarrdic,k2,code = CAF.code_level_gen_even(j)
        Hmax = CAF.Hmax_gen(eledic, lensarrdic, j)
        pairs = CAF.All_pairs(k2)
        Hxy, probx, probxy =CAF.Hse_len(eledic, lensdic, lensarr,je)
        cprobxy = CAF.combined_probxy(probx, probxy,lensdic, lensarr,eledic)
        Hxyx, probxyx =CAF.hselen_re_even(eledic, lensdic, pairs, lensarr, cprobxy,code)
        cprobxyx = CAF.combined_probxyx(cprobxy,probxyx,lensdic, lensarr,eledic)
        Hxyxy, probxyxy = CAF.hselenre_len_even(cprobxyx,eledic, lensdic,pairs, lensarr,code)
        Htotal = 0
        Htotal = Hmax + Hxy + Hxyx + Hxyxy
        
        return Htotal, je

    def complex_level_odd(j):
         jo, lensarr, eledic, lensarrdic,lensdic,k1,code=CAF.code_level_gen_odd(j)
         Hmax = CAF.Hmax_gen(eledic, lensdic, j)
         pairs = CAF.All_pairs(k1)
         Hxy, probx, probxy =CAF.Hse_len(eledic, lensarrdic, lensarr,jo)
         cprobxy = CAF.combined_probxy(probx, probxy,lensarrdic, lensarr,eledic)
         Hxyx, probxyx = CAF.hselen_re(eledic, lensarrdic, pairs, lensarr, cprobxy, code)
         cprobxyx = CAF.combined_probxyx(cprobxy,probxyx,lensarrdic, lensarr,eledic)
         Hxyxy, probxyxy = CAF.hselenre_len(cprobxyx,eledic, lensarrdic,pairs, lensarr, code)
         Htotal = 0
         Htotal = Hmax + Hxy + Hxyx + Hxyxy
         return Htotal,jo
         
    def check_for_end(j,bin_arr,code_level,c):
        if(code_level % 2) == 0:
            k = CAF.code_level_gen_even_check(j)
            if(k[0] == bin_arr[c]):
                code_level = 0
            else:
                code_level = code_level
        elif(code_level % 2 ) != 0:
            k = CAF.code_level_gen_odd_check(j)
            if(k[0] == bin_arr[c]):
                code_level =0
            else:
               code_level = code_level
               
        return code_level
         
    #cycle length
    bin_arr = CAF.cycle_patterns(n)
    #Dictionary to add complexities
    complexity = CAF.cycle_complex_dictionary(bin_arr)

    for c in range(len(bin_arr)):
        H = []
        code_level = 1
        Htotal,jo = complex_level1(bin_arr,c)
        H.append(Htotal)
        code_level = code_level +1
        
        
        while (code_level>0):
            if(code_level % 2) == 0:
                code_level = check_for_end(jo,bin_arr,code_level,c)
                if(code_level ==0):
                    break
                Htotal, je  = complex_level_even(jo)
                H.append(Htotal)
                code_level = code_level +1
            else:
                code_level = check_for_end(je,bin_arr,code_level,c)
                if(code_level ==0):
                    break
                Htotal,jo = complex_level_odd(je)
                H.append(Htotal)
                code_level = code_level +1


        Hcomplex = 0
        for i in(H):
            Hcomplex = Hcomplex + i
        complexity[bin_arr[c]] = Hcomplex
        
    return complexity
    
             
def write_to_csv(i):
    complexity = complexity_of_cycle(i)
    max_key = max(complexity, key=lambda k: complexity[k])
    bias = complexity[max_key]
    o = str(i)
    block = len(complexity)/2
    check_block = 0
    for i in complexity:
       if (complexity[i] ==0.0):
           continue
       if(check_block == block):
           break
       else:
           complexity[i] = complexity[i] +bias
           check_block = check_block+1
    complexity1 = dict(sorted(complexity.items(), key=lambda item: item[1]))
    with open('/Users/noelalben/Desktop/Proj2020/Main Proj File Codes/CSV_Complexity/compdict23'+o+'.csv', 'w') as csv_file:
         writer = csv.writer(csv_file)
         for key, value in complexity1.items():
            writer.writerow([str(key), value])
    return complexity1
    
def read_write_csv(i):
    o = str(i)
    name = '/Users/noelalben/Desktop/Proj2020/Main Proj File Codes/CSV_Complexity/compdict'+o+'.csv'
    with open(name) as f:
         d = dict(filter(None, csv.reader(f)))
    return d
         

            


