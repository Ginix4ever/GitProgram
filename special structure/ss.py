from collections import Counter
len_as = input()
len_a = int(len_as)
all_data = []
arr_b = []
for _ in range(len_a):
    str_b = input()
    arr_b = str_b.split(' ')
    for i in range(int(arr_b[0]), int(arr_b[1]) + 1):
        if int(arr_b[0]) == int(arr_b[1]):
            all_data.append(int(arr_b[0]))
            break
        all_data.append(i)
nummap = Counter(all_data)
# print(nummap)
uniq_data = list(set(all_data))
uniq_data.sort()
for d in uniq_data:
    print("%s %s" %(d, nummap.get(d)))