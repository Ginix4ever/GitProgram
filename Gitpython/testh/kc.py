import heapq
from collections import deque

def list_merge(*lists):
    #入参判断, 这里直接pass
    #将所有链表转化为deque,方便使用popleft获取链表的最左元素及根据索引返回该索引对应的剩余链表
    queues = [queue for queue in map(deque, lists)]
    heap = []
    #初始化链表,该链表中的元素为元组, 各个链表的第一个元素及链表所在索引
    for i, lst in enumerate(queues):
        heap.append((lst.popleft(), i))
    #将链表转换成最小堆
    heapq.heapify(heap)
    #链表: 用于存放每次获取的堆顶层元素
    result = []
    
    while heap:
        #将堆顶层元素出堆
        value, index = heapq.heappop(heap)
        #将顶层元素追加
        result.append(value)
        #根据索引获取对应链表的剩余元素
        if queues[index]:
             #如果存在下一个元素,则将该元素及索引入堆
            heapq.heappush(heap, (queues[index].popleft(), index))
    return result


q= list_merge(*[[4, 8, 20], [100, 200, 350, 370], [5, 8, 350, 500, 1000]])
print (q)