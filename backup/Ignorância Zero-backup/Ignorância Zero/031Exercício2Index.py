a = [1,2,3,3,5]

n = int(input("Digite um elemento: "))
"""
b = []
cont = 0
for i in range(len(a)):
    if a[i] == n :
        b.append(cont)
    cont += 1
if b == []:
    print("Elemento não encontrado!")
else:
    print("Índice:",b[0])
"""
b = 0
for i in range(len(a)):
    if a[i] == n:
        b = 1
if b == 0:
    print("Elemento não encontrado!")
else:
    print("Índice:",a.index(n))

