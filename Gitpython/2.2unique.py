def compress(data):
    sum = {}
    for d in data:
        if d in sum.keys():
            sum[d] += 1
        else:
            sum[d] = 1
    res = []
    for k,v in sum.items():
        tmp = (k, v)
        res.append(tmp)

    return res

res = compress([1, 2, 1, 3])
print(res)