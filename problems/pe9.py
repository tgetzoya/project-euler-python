# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# Answer: 31875000


def run():
    for idx in range(1, 996):
        for jdx in range(1000 - idx, 0, -1):
            for kdx in range(1000 - idx - jdx, 0, -1):
                if idx + jdx + kdx == 1000:
                    if idx ** 2 + jdx ** 2 == kdx ** 2:
                        return idx * jdx * kdx
