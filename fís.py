X = float(input("escreva algo:"))

v = 90 + 90 * (6.6 *(10**-5)) * 50 - (X + X *(1.3 *(10**-4)) * 50) 
f = 90 * (6.6 *(10**-5)) * 50 - (X * (1.3 *(10**-4)) * 50)
print(v)
print(f)
if v == f:
    print("yes")