s = input('s: ')
t = input('t: ')

for i in range(0, len(s) - len(t)):
    if s[i:i+len(t)] == t:
        print(i+1)