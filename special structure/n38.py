def count(num, arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= num:
            start = mid + 1
            if start > end:
                return end + 1
        else:
            if mid == 0:
                return 0
            if arr[mid - 1] > num:
                end = mid - 1
            else:
                return mid
    return 0
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
   # times = int(input())
    left = []
    right = []

    lins = int(input())
    # 边界节点5
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
        
        arraypointleft.append(a)
        arraypointright.append(b)

    arraypointleft.sort()
    arraypointright.sort()
    for i in range(arraypointleft[0], arraypointright[lins - 1] + 1):
        ans = count(i, arraypointleft) - count(i - 1, arraypointright)
        if ans != 0:
            print(i, " ", ans)