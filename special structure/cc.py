
len_as = input()
str_a = input()
a = str_a.split(' ')
len_bs = input()
str_b = input()
b = str_b.split(' ')
a.extend(b)

a=[ int(x) for x in a]
c=sorted(a,reverse=False)

for i in c:
    print(i,end=' ')