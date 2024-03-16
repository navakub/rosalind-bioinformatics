import os.path

filename = os.path.abspath('./python-village/ini5.txt')
f = open(filename, 'r')

i = 1
for line in f.readlines():
    if i % 2 == 0 :
        print(line)
    i += 1