# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 906609

def run():
    return largest_palindrome(3)


def largest_palindrome(digits):
    range_of_numbers = (10 ** digits)

    max = -1

    for idx in range(range_of_numbers - 1, int(range_of_numbers / 10), -1):
        for jdx in range(range_of_numbers - 1, int(range_of_numbers / 10), -1):
            kdx = idx * jdx
            kdxs = str(kdx)
            if kdxs == kdxs[::-1] and kdx > max:
                max = kdx

    print(max)
