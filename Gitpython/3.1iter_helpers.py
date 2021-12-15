import itertools
from _operator import mul

def transpose(data):
    return list(zip(*data))

res = transpose([[1,2],[3,-1]])
print(res)



def transpose(it):
    return itertools.zip_longest(it[0], it[1])


def scalar_product(a, b):
    a1 = []
    a2 = []
    for i in a:
        if type(i) == int or type(i) == float:
            a1.append(i)
        elif type(i) == str:
            if i.isdigit():
                a1.append(float(i))
            else:
                return None
        else:
            return None
    for i in b:
        if type(i) == int or type(i) == float:
            a2.append(i)
        elif type(i) == str:
            if i.isdigit():
                a2.append(float(i))
            else:
                return None
        else:
            return None
    return sum(itertools.starmap(mul, itertools.zip_longest(a1, a2)))

