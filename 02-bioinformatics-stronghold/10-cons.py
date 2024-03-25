from os import path

script_dir = path.dirname(__file__) #<-- absolute dir the script is in
rel_path = '10-cons.fas'
abs_file_path = path.join(script_dir, rel_path)


with open(abs_file_path) as f:
    contents = f.readlines()
    contents = list(filter(lambda x: x[0] != '>', contents))
    contents = [list(s.replace('\n', '')) for s in contents]
    
print(contents)
dnas = []
profile_matrix = []

for i in range(len(contents[0])):
    dna = [x[i] for x in contents]
    dnas.append(dna)

    count_a = dna.count('A')
    count_c = dna.count('C')
    count_g = dna.count('G')
    count_t = dna.count('T')

    profile_matrix.append([count_a, count_c, count_g, count_t])

profile_matrix = [[row[i] for row in profile_matrix] for i in range(len(profile_matrix[0]))]

consensus = ''
code = 'ACGT'

for i in range(len(profile_matrix[0])):
    counts = [x[i] for x in profile_matrix]
    idx = counts.index(max(counts))
    c = code[idx]
    consensus += c


print(consensus)
for i in range(0,4):
    print(code[i]+ ': ', end='')
    print(*profile_matrix[i])