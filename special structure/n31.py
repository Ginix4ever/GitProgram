import numpy as np
def getNumbers(a,b,arrayn):
    for i in range(a,b+1):
        arrayn[i-1]+=1

if __name__ == '__main__':

    lins=int(input())
    #保存原始数组
    arrayL=""
    #保存新数组
    arrayN=[0]*100000
    for i in range(0,lins):
        #listn = input("")
        a,b = (input("").split())
        a=int(a)
        b=int(b)
        getNumbers(a,b,arrayN)

    # arrayL=np.nonzero(arrayN)

    # for j in range(0,len(arrayN)):
    #     if(arrayN[j]!=0):
    #         print("%d %d" %(j+1,arrayN[j]))

    #print("#########")
    
    #print(arrayN)


    arrayL=np.nonzero(arrayN)

    t = int(arrayL[0].size)

    for l in range(0,t):
        s1 = str(arrayL[0][l]+1)
        s2 =arrayN[arrayL[0][l]]
        print("%s %s" %(s1,s2))

    #print(arrayL)

    #print(arrayL[0])