
def getnumber(n):

    if(n==1):
        return 1
    if(n==0):
        return 0
    else:
        return (getnumber(n-1)+getnumber(n-2))






if __name__ == '__main__':

    print("请输入数字")
    n = input()
    k= getnumber(int(n))

    print("结果为")
    print(k)