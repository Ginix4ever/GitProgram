def merge_sort(arya, aryb):
        indexa = 0
        indexb = 0
        li = []
        while indexa < len(arya) and indexb < len(aryb):
                if arya[indexa] <= aryb[indexb]:
                        li.append(arya[indexa])
                        indexa += 1
                else:
                        li.append(aryb[indexb])
                        indexb += 1
        li = li + arya[indexa:] + aryb[indexb:]
        return li


if __name__ == '__main__':
    
    #ty=input("")
    listn=input("")

    ln=[int(n) for n in listn.split()]
    #y=input("")

    listn=input("")
    lnN=[int(n) for n in listn.split()]
    a =merge_sort(ln,lnN)

    str1=""

    for i in a:
        str1=str1+str(i)+" "
    print(str1)