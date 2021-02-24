n=1000


while n <10000:
    m=n//100
    d=n % 100
    t= m + d
    if t**2 == n:
        print(n)
    n += 1
