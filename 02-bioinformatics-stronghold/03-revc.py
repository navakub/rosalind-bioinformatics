s = input('dna strings: ')

s_rev = s[::-1]
complement = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}

i = 0
sc = ''
for c in s_rev:
    sc += complement[c]
    i += 1

print(sc)