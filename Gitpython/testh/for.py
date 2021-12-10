import heapq
from collections import deque

def list_merge(*lists):
   
    queues = [queue for queue in map(deque, lists)]
    heap = []
   
    for i, lst in enumerate(queues):
        heap.append((lst.popleft(), i))
   
    heapq.heapify(heap)
    
    result = []
    
    while heap:
      
        value, index = heapq.heappop(heap)
        
        result.append(value)
        
        if queues[index]:
            
            heapq.heappush(heap, (queues[index].popleft(), index))
    return result




if __name__ == '__main__':
     
    ty=input("")
    listn = input("")

    ln = [int(n) for n in listn.split()]
    ty=input("")
    #print("input another list or tuple")
    listn = input("")
    lnN = [int(n) for n in listn.split()]
   # a = list_merge(*[ln,lnN])
    #print (a)
    a = ln+lnN
    a.sort
    str1=""

    for i in a:
        str1=str1+str(i)+" "
    print(str1)