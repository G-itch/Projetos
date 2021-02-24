n1= int(input("Digite um número inteiro não-negativo:"))
cont=0
produto=1
n2 = n1
while cont < n1 :
    produto = produto * n1
    n1 = n1 - 1

print("O fatorial de",n2,"é",produto)