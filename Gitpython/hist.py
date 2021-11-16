def distribute(arry, k):
    for i in range(0, len(arry), 1):
        for j in range(i+1, len(arry), 1):
            if(arry[i] > arry[j]):
                temp = arry[i]
                arry[i] = arry[j]
                arry[j] = temp
    
    strT = ""
    c=1
    for i in range(0, len(arry)):
        if(c < k):
            strT += str(arry[i])+","
            c+=1
            continue
        if(c == k):
            strT += str(arry[i])+" ] ["
            c=0
            #if(len(arry)-1-i<k)
            continue
    
    strT ="["+strT+"]"
    
    print(strT)


if __name__ == '__main__':

    arry = input("")
    numN = [int(n) for n in arry.split()]

    print("input number of k")
    num = int(input())

    distribute(numN,num)
   # print(numN)
