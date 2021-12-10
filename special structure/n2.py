

ty = input("")
listn = input("")

number_list = [int(n) for n in listn.split()]
al = len(number_list)
k = 0
c = 0
sign=0
for i in range(len(number_list)-2, -1, -1):
    # print(i)
    if number_list[i+1] == number_list[i]:
        k += 1
        c +=1
        sign=1
        number_list.remove(number_list[i+1])
    else:
        if(sign==1):
            number_list.remove(number_list[i+1])
            sign=0




print(len(number_list))
