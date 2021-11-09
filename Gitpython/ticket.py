# datetime
# coder ginix
# sumnum 加法迭代次数计数器
def get_nearest_lucky_ticket(ticketnumber, isadd=True, sumnum=0, subnum=0):

    # 存放计数器，用于存放使用了多少次加法迭代，相应的减法迭代次数 少于加法次数 就是 绝对值更小
    #consitnNum = sumnum;

    listn = [int(x) for x in (ticketnumber)]

    # saved odds and evens
    odds = 0
    evens = 0

    for i in range(0, len(listn)):

        if i % 2 == 0:
            evens += listn[i]
        else:
            odds += listn[i]

       # print(listn[i])

    if (odds == evens):
        return [ticketnumber, sumnum]
    else:
        sumnum += 1

        if(subnum != 0):
            if(subnum<sumnum):  # 这里没有考虑如果正负同步的问题。
                return  [-1]

        # print("离您最接近的号码是：")
        if(isadd == True):
            k = int(ticketnumber)+1
        else:
            k = int(ticketnumber)-1
        # return 1;
        return get_nearest_lucky_ticket(str(k), isadd, sumnum,subnum)

    #print ( [int (x) for x in str(ticketnumber)])

    ##print (ticketnumber )


def get_nearest_lucky_ticket_n(ticketnumber):

    return 0


if __name__ == '__main__':

    #
    ticketnumber = input("请输入彩票号码：")
    rightn = get_nearest_lucky_ticket(ticketnumber)
    if(ticketnumber == rightn[0]):
        print("恭喜您中奖了，彩票号码是：")
        print(ticketnumber)
        print("--------")
        print(rightn[1])
    else:
        print("离您最近的号码是：")

        negnum = get_nearest_lucky_ticket(ticketnumber, False, 0,rightn[1])

        if(negnum[0] == -1):
            print(rightn[0])
            print("-----step")
            #print(negnum[1])
        else:
            print(negnum[0])
            print("-----step")
            print(negnum[1])
