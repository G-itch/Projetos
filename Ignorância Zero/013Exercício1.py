n1 = int(input("Digite a base: "))
n2 = int(input("Digite o expoente: "))
cont = 0
produto = 1
while cont < n2:
    produto = produto*n1
    cont = cont + 1

print("base:",n1,"expoente:",n2,"resultado:",produto)