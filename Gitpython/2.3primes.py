def get_primes(num):
    lst = []
    if num <= 1:
        return '0 ~ %d以内没有任何素数' % num
    for i in range(2, num + 1):
        for j in range(2, int(i / 2) + 1):
            if not i % j:
                break
        else:
            lst.append(i)
    return lst

res = get_primes(11)
print(res)
