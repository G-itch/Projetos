n = float(input("Digite um número: "))

if n == int(n):
    print("O número é inteiro")
else:
    if n - int(n) <= 0.5:
        r = round(n + 1)
    else:
        r = round(n)
    print("O número é real")
    print("O número arredondado é igual a %r, %i" %(r, int(n+1)))