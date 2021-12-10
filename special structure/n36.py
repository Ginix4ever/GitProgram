import numpy as np
#查找第一个大于等于给定值的元素
def bSearchV3(s, k):
    low = 0
    high = len(s) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if s[mid] < k:
            low = mid + 1
        else:
            if mid == 0 or s[mid - 1] < k:
                return mid
            else:
                high = mid - 1
    return -1
#查找最后一个小于等于给定值的元素
def bSearchV4(s, k):
    low = 0
    high = len(s) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if s[mid] <= k:
            if mid == len(s) - 1 or s[mid + 1] > k:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return -1


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

    # while(i<=maxpoint):
    #     result = bSearchV4 (arraypointleft,4) 
    #     for j in range(0,result+1):
    #         if(arraypointright[j]>=i):
    #             tempN+=1
    #     if(tempN!=0):
    #         print("%d %d " %(i,tempN))
    #     tempN=0
    #     i+=1`
    result = bSearchV4 (arraypointleft,4) 
    result2  = bSearchV3 (arraypointright, 4) 
    
    print("---binsearchL")
    print(result)
    print("---binsearchR")
    print(result2)
    print("---arraypointleft")
    print(arraypointleft)
    print("---arraypointright")
    print(arraypointright)
    # print("---maxpoint")
    print(maxpoint)


