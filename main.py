import timeit

from problems import pe29


def main():
    start = timeit.default_timer()
    print(pe29.run())
    end = timeit.default_timer()
    print("{} Seconds".format(format(end - start, '.4g')))


if __name__ == "__main__":
    main()
