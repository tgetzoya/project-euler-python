# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this
# value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
# 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
#
# Answer: 871198282

def run():
    text_file = open("/home/tgetzoyan/Documents/p022_names.txt", "r")
    lines = text_file.read().split(',')
    text_file.close()

    sum = 0

    for idx, line in enumerate(sorted(lines)):
        sum += (idx + 1) * word_to_number(line)

    return sum


def word_to_number(word):
    return sum((ord(ch) - 64) for ch in word if ord(ch) > 64)
