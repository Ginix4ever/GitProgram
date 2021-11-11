
def calculate_special_sum(number):

    if(number <= 2):
        return number

    sum1 = 0
    for x in range(1, int(number+1), 1):
        #print(x)
        #print(x*(x-1)*(x-1))
        sum1 = int(x*(x-1)*(x-1))+int(sum1)
        print(sum1)
    return sum1


if __name__ == '__main__':

    numberN = int(input())

    print(calculate_special_sum(numberN))
