def get_triangle_number(num):
    sum = 0
    for idx in range(1, num + 1):
        sum += idx
    return sum
