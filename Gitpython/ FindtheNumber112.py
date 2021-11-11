# get input number
def getNumberFromInput(arrayS, lenth):
    for i in range(lenth):
        arrayS.append(int(input()))
    return None


def findnumber(array, mlines):

    isInOrNot = []

    for i in range(mlines):
        tempNumber = int(input())
        if(tempNumber in array):
            isInOrNot.append("FOUND")
        else:
            isInOrNot.append("MISSED")

    return isInOrNot


if __name__ == '__main__':

    # tip
    print("input lenth of array:")
    # lenth
    arraylenth = int(input())
    # rec array
    arry = []

    #getNumberFromInput(arry, arraylenth)

    arry = input("")
    numN = [int(n) for n in arry.split()]

    mLines = int(input())

    result = findnumber(numN, mLines)

    for str in result:
        print(str)
