lines = int(input())
array = sorted(map(int, input().split()))
m = int(input())
arrayn = []
for i in range(m):
    x = int(input())
    arrayn.append(x)
for i in arrayn:
    L = 0
    R = lines - 1
    ans = -1
    while L <= R:
        mid = (R - L >> 1) + L
        if i > array[mid]:
            ans = mid
            L = mid + 1
        else:
            R = mid - 1
    if ans == -1:
        print(array[0])
    else:
        if ans + 1 > lines - 1:
            print(array[ans])
        elif i - array[ans] <= array[ans + 1] - i:
            print(array[ans])
        else:
            print(array[ans + 1])