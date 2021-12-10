from ast import Str
import typing


def marges(arry, arryN):

    arryPrint=[]
    
    for i in range(0,len(arry)):
        j=0
        k=0
        while(j<len(arryN)):
            
            if(arry[i]>arryN[j]):
                 if((i==(len(arry)-1))&(j==(len(arryN)-1))):
                    arryPrint.append(arry[i])
                    break
                 else:
                    arryPrint.append(arryN[j])
                    del arryN[j]
                    j=0
            else:
                if(i==(len(arry)-1)):
                    if(k==0):
                        arryPrint.append(arry[i])
                        k=1
                    arryPrint.append(arryN[j])
                    j+=1
                    #j+=1
                    #if(j>=len(arryN)):
                        #arryPrint.append(arryN[j-1])
                    continue
                arryPrint.append(arry[i])

                if((i==(len(arry)-1))&(j==(len(arryN)-1))):
                    arryPrint.append(arryN[j])
                    break
                else:
                    #arryPrint.append(arry[i])
                    j+=1
                break
            

    
    #print (arryPrint)
    return (arryPrint)


if __name__ == '__main__':

   # print("input an list or tuple")
    ty=input("")
    listn=input("")

    ln=[int(n) for n in listn.split()]
    ty=input("")
    #print("input another list or tuple")
    listn=input("")
    lnN=[int(n) for n in listn.split()]

    alist= marges(ln, lnN)


    str1=""

    for i in alist:
        str1=str1+str(i)+" "
    #str =""
    print(str1)

