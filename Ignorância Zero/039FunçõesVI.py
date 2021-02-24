def fatorial(n):
    fat = 1
    for i in range(1,n+1):
        fat *= i
    return fat

print(fatorial(7))

def fat2(n):
    if n == 1:
        return n
    return fat2(n-1) * n

print(fat2(7))