len_as = input()
str_b = []
all_data = []
for i in range(int(len_as)):
    str_b.append(input().split(' '))
del len_as
for i in str_b:
    all_data += [j for j in range(int(i[0]), int(i[1]) + 1)]
del str_b
all_data.sort()
nummap = {}
for i in all_data:
    if i in nummap:
        nummap[i] += 1
    else:
        nummap[i] = 1
del all_data
for k,v in nummap.items():
    print(f"{k} {v}")