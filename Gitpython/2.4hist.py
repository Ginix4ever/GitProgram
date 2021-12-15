def distribute(histogram, randk):
    list = [0] * randk
    min_ = min(histogram)
    max_ = max(histogram)
    interval = (max_ - min_) / randk
    for i in histogram:
        index = int((i - min_) / interval)
        if (i - min_) != 0 and (i - min_) % interval == 0:
            index -= 1
        list[int(index)] += 1
    return list


