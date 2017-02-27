def run():
    sum = 0
    for idx in range(1, 1000):
        if idx % 5 == 0:
            sum += idx
        elif idx % 3 == 0:
            sum += idx
    return sum
