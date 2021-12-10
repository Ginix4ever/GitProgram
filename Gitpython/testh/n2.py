def find(array):
    i=0
    #记录重复个数，比实际个数少一
    sum=0
    #记录重复次数，用次数乘以1 为减少个数
    k=0
    while(i<(len(array)-1)):
        if(array[i]==array[i+1]):
            #
            sum+=1
            #判读是否为最后一项
            if((i+1)==(len(array)-1)):
                k+=1
                
                break
            elif((i+2)<=(len(array)-1)):
                if(array[i+1]==array[i+2]):
                  
                    i+=1
                else:
                    k+=1
                    i+=1

            continue

        i+=1

    print(len(array)-sum-k)
   # print ((sum+k))
    return array

if __name__ == '__main__':
    
    #ty=input("")


    a = find(ln)

    #for i in a:
        #str1=str1+str(i)+" "
    #print(a)