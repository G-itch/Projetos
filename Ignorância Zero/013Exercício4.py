print("Digite um número inteiro que eu direi a soma de todos os números inteiros até ele:" )

n1 = int(input("Digite um número:"))
cont = 1
cont1 = 1
while cont1 < n1:
    cont = cont + (cont1+1)
    cont1 = cont1 + 1


print(cont)