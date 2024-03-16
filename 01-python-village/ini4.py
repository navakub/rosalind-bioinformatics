a = int(input('a: '))
b = int(input('b: '))

res = 0
if a > 0 and b > 0 and a < b and b < 10000:
    if a%2==0:
        for i in range(a+1, b+1, 2):
            res += i
    else:
        for i in range(a, b+1, 2):
            res += i

print(res)
