import gc 
from collections import Counter
#import pandas as pd
#方法一，展开 然后归纳 数据项重复次数
if __name__ == '__main__':
    #print("input lines")
    #lines
    lins=int(input())
    #保存原始数组
    arrayL=[]
    #保存新数组
    arrayN=[]
    for i in range(0,lins):
        #listn = input("")
        a,b = (input("").split())
        a=int(a)
        b=int(b)
        #arrayL.append([int(n) for n in listn.split()])
        #tmp= [int(n) for n in listn.split()]
        #k=int(input())
        #print(k)
        #l=int(input())
        #print(l)
        for j in range(a,b+1):
            arrayN.append(j)
    #mylist=[1,2,2,2,2,2,2,3]
        #arrayN.sort()
    #arrayN=arrayN.sort()
    myset = set(arrayN)
    for item in myset:
	    print("%d %d" %(item,arrayN.count(item)))


    #print(arrayL)
    #print(arrayN)

    #arrayN.sort()



    #print(arrayN)
    #print("input lines")
    #dict={}
    #for key in arrayN:
       # dict[key]=dict.get(key,0)+1
    #for key in dict:
       # print(str(key)+' '+str(dict[key]))
    #result =pd.value_counts(arrayN)
    #result.sort_index()
    #print(result.sort_index())
    #print (dict)
   
   
   
  
    
    #print(sorted(arrayN.items()))
  
  # arrayN=Counter(arrayN)
    # strn= str(sorted(arrayN.items()))
    # del arrayN
    # gc.collect()
    # strn=strn.replace("[","")
    # strn=strn.replace(" (","")
    # strn=strn.replace("),","\n")
    # strn=strn.replace("(","")
    # strn=strn.replace(",","")
    # strn=strn.replace(")]","")
    # print(strn)

#number_list = [int(n) for n in arrayL.split()]
#print(number_list)
