def getnumber(n):

    if n<=1:
        return 1
    #if(n<=1):
      #  return n
    #else:
        #return (getnumber(n-1)+getnumber(n-2))
    f0=0 
    f1=1
    temp=0
    for i in range(1,n,1):
        temp=f0+f1
        f0=f1
        f1=temp
    
    return f1

if __name__ == '__main__':


    k= getnumber(int(input()))
    print(k)