from utils.factors import get_factors


def run():
    map = {}
    sum = 0
    for idx in range(1, 100):
        map[idx] = sum(get_factors(idx, True))
    for key, value in map.items():
        if (value in map) and (map[value] == key):
            sum += key + value
            del map[key]
            del map[value]
