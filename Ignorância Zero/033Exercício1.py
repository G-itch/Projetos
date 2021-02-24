def pot(n,p):
    pot = 1
    for i in range(p):
        pot *=n
    return pot,i

a,b = pot(2,5)
print(a)