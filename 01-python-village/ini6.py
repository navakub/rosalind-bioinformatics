from collections import Counter

text = input('text: ')
# 'We tried list and we tried dicts also we tried Zen'

for key,val in Counter(text.split()).items():
    print(key, val)
