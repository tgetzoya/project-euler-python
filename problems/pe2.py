def run():
    x = 1
    y = 2
    sum = 2
    while y < 4000000:
        hold = x
        x = y
        y = x + hold
        if y % 2 == 0:
            sum += y
    return sum
