from collections import Counter

s = input('dna string: ')

count_syms = sorted(Counter(s).items())
for _, val in count_syms:
    print(val, end=' ')

