if __name__ == '__main__':
    # for i  in range(1,5,2):
    # print(i,i+1,end=' ')
   # print(dir(object))

    # python
    nterms = int(input())

F1 = 0
F2 = 1
count = 2

if nterms <= 0:
    print(F1)
elif nterms == 1:
    print(F1)
else:
    #print(F2)
    while count < nterms:
        nth = F1 + F2
     
        F1 = F2
        F2 = nth
        count = count + 1
    print(F2)