
def calculate_special_sum(num):
    if num == 0:
        return 0
    sum = pow(num-1, 2) * num
    sum += calculate_special_sum(num - 1)
    return sum

ru = calculate_special_sum(2)
print(ru)

