from ast import Str
import typing


def marges(arry, arryN):

    arryPrint = []
    k=0
    l=0
    for i in range(0, len(arry)):
        for j in range(l, len(arryN)):

            if((arry[i] <= arryN[j]) & (i != (len(arry)-1))):
                arryPrint.append(arry[i])
                # if(i==(len(arry)-1)):
                # arryPrint.append(arryN[j])

                break
                # if(i==(len(arry)-1)):
                # arryPrint.append(arryN[j])
                # continue
                # else:
                # arryPrint.append(arry[i])
                # break
            if(arry[i] > arryN[j]):
                arryPrint.append(arryN[j])
                
                if(j == (len(arryN)-1)):
                    arryPrint.append(arry[i])
                continue

            # 判断i的最后一项
            if(i == (len(arry)-1)):

                if(k==0):
                    arryPrint.append(arry[i])
                    k=1
                

                if(arry[i] <= arryN[j]):
                    arryPrint.append(arryN[j])
                    continue
            # if((i==(len(arry)-1))&(j==(len(arryN)-1))):
              # arryPrint.append(arry[i])

            # elif(i==[len(arry)-1]):
            # arryPrint.append(arry[i])
            # elif(j==[len(arryN)-1]):
            # arryPrint.append(arryN[j])
            # else:
            # arryPrint.append(arryN[j])

    return(arryPrint)


if __name__ == '__main__':

   # print("input an list or tuple")
    #ty=input("")
    listn=input("")

    ln=[int(n) for n in listn.split()]
    #ty=input("")
    #print("input another list or tuple")
    listn=input("")
    lnN=[int(n) for n in listn.split()]

    alist= marges(ln, lnN)

    str1=""

    for i in alist:
        str1=str1+str(i)+" "
    #str =""
    print(str1)
    #str=str(alist[1])

    #str="["
    #for  i in range(0,len(alist)):
        #str=str+str(alist[i])+","
    
    #print(str)

   # print(ln)
