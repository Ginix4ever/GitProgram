import numpy as np

#不小于某数的第一个元素
def binsearchR(l, e, lo, hi):
    while lo < hi-1:
        mi = (lo + hi)//2
        if e >= l[mi]: lo = mi
        else: hi = mi
    return lo
#不大于某数的最后一个元素
def binsearchL(l, e, lo, hi):
    while lo < hi-1:
        mi = (lo + hi)//2
        if e >= l[mi]: lo = mi
        else: hi = mi
    return lo

# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binarySearch (arr, l, r, x): 
  
    # 基本判断
    if r >= l: 
  
        mid = int(l + (r - l)/2)
  
        # 元素整好的中间位置
        if arr[mid] == x: 
            return mid 
          
        # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # 元素大于中间位置的元素，只需要再比较右边的元素
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        # 不存在
        return -1



if __name__ == '__main__':

    lins = int(input())
    # 边界节点
    arraypointleft = []
    # 边界节点
    arraypointright = []
    # 保存新数组
    arrayN = []
    # 确定最大边界节点
    maxpoint = 0
    for i in range(0, lins):
        #listn = input("")
        a, b = (input("").split())
        a = int(a)
        b = int(b)
        
        if(b>maxpoint):
            maxpoint=b


        arraypointleft.append(a)
        arraypointright.append(b)
    
    i=1
    #记录次数
    tempN=0
    # while(i <=maxpoint):
    #     for j in range(0,lins):
    #         # if(i>=arraypointleft[j] and i<=arraypointright[j]):
    #         #         tempN+=1
    #         binarySearch(arr, 0, len(arr)-1, x) 
    #     if(tempN!=0):
    #         print("%d %d " %(i,tempN))
    #     tempN=0
    #     i+=1

    # while(i<=maxpoint):
        
    #     result = binarySearch (arraypointleft, 0, len(arraypointleft)-1, i) 

    #     if(result!=-1):
    #         break;
    while(i<=maxpoint):
        result = binsearchL (arraypointleft, i, 0, len(arraypointleft)) 
        for j in range(0,result+1):
            if(arraypointright[j]>=i):
                tempN+=1
        if(tempN!=0):
            print("%d %d " %(i,tempN))
        tempN=0
        i+=1

    #result2  = binsearchR (arraypointright, 5, 0,len(arraypointleft)) 
    
    # print("---binsearchL")
    # print(result)
    # print("---binsearchR")
    # #print(result2)
    # print("---arraypointleft")
    # print(arraypointleft)
    # print("---arraypointright")
    # print(arraypointright)
    # print("---maxpoint")
    # print(maxpoint)

    # for j in range(0,len(arrayN)):
    #     if(arrayN[j]!=0):
    #         print("%d %d" %(j+1,arrayN[j]))

    # arrayL=np.nonzero(arrayN)

    # t = int(arrayL[0].size)

    # for l in range(0,t):
    #     s1 = str(arrayL[0][l]+1)
    #     s2 =arrayN[arrayL[0][l]]
    #     print("%s %s" %(s1,s2))
