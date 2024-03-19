k = int(input('k: '))
m = int(input('m: '))
n = int(input('n: '))

pop = k+m+n
print(1 
      - n/pop * (n-1)/(pop-1)
      - 1/4 * m/pop * (m-1)/(pop-1)
      - 1/2 * m/pop * n/(pop-1)
      - 1/2 * n/pop * m/(pop-1)
      )