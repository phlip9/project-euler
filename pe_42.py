# find the number of triangle words in the list of words

triangle_nums = set([int((n * (n + 1)) / 2) for n in range(1, 100)])

words = next(open("words.txt"))[1:-1].split('","')

def is_tri_num(word):
    return sum(map(lambda c: ord(c) - 64, word)) in triangle_nums

print(len(list(filter(is_tri_num, words))))
