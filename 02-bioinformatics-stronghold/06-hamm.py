s = input('dna: ')
t = input('another dna: ')

if len(s) == len(t) and len(s) < 1000 and len(t) < 1000:
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1

    print(count)