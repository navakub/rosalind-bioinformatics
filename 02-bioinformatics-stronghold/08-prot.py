from os import path

script_dir = path.dirname(__file__) #<-- absolute dir the script is in
rel_path = '08-rnacodon.txt'
abs_file_path = path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    codon2prot = dict()
    for line in f.readlines():
        line = line.split()
        codons = line[::2]
        prots = line[1::2]
        for i, codon in enumerate(codons):
            codon2prot[codon] = prots[i] 

s = input('rna: ')


protein = ''
for i in range(0, len(s), 3):
    prot = codon2prot[s[i:i+3]]
    if prot != 'Stop':
        protein += prot
    else: 
        break
print(protein)
