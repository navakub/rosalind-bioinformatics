from os import path

script_dir = path.dirname(__file__) #<-- absolute dir the script is in
rel_path = '05-gc.fas'
abs_file_path = path.join(script_dir, rel_path)

label_list = []
gc_list = []
with open(abs_file_path) as f:
    contents = f.readlines()
    
    dna = ''
    gc = 0

    for i, content in enumerate(contents):
        if content.startswith('>'):
            label = content[1:-1]
            label_list.append(label)
        else:
            dna += content.replace('\n', '')
            if i == len(contents) - 1 or contents[i+1].startswith('>'):
                gc = 100*(dna.count('G') + dna.count('C'))/len(dna)
                gc_list.append(gc)
                dna = ''
                gc = 0

idx = gc_list.index(max(gc_list))

print(label_list[idx])
print(f'{gc_list[idx]:.6f}')