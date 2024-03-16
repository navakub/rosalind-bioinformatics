from os import path
from collections import Counter

script_dir = path.dirname(__file__) #<-- absolute dir the script is in
rel_path = '05-gc.fas'
abs_file_path = path.join(script_dir, rel_path)

label_list = []
gc_list = []
with open(abs_file_path) as f:
    for dna in f.readlines():
        if dna[0] == '>':
            label = dna[1:-1]
            label_list.append(label)
        else:
            gc = 100 * (dna.count('G') + dna.count('C'))/ len(dna)
            gc_list.append(gc)

idx = gc_list.index(max(gc_list))

print(label_list[idx])
print(f'{gc_list[idx]:.6f}')
