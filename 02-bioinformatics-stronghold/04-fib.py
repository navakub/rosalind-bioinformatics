n = int(input('n: '))
k = int(input('k: '))

def rabbits(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rabbits(n-1, k) + k*rabbits(n-2, k)
    
print(rabbits(n,k))
