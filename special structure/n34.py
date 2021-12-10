if __name__ == '__main__':
    lineinput = int(input())
    array = {}
    for i in range(lineinput):
        a,b = (input("").split())
        a=int(a)
        b=int(b)
        # str_b = input()
        # arr_b = str_b.split(' ')
        for i in range(int(a), int(b) + 1):
            if i in array.keys():
                array[i] += 1
            else:
                array[i] = 1
    newa = sorted(array.keys())
    for i in newa:
        print("%s %s" %(i, array.get(i)))
 