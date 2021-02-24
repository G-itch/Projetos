Par = []
Impar = []
for i in range(1,21):
    n = int(input("Digite o %i número de 20: " %i))
    if n%2 == 0 :
        Par.append(n)
    else:
        Impar.append(n)

print("Os números pares são :",Par)
print("Os números impares são :",Impar)

