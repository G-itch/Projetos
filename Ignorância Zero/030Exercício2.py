números = []
seq = int(input("Digite o número de elementos da lista:"))
for i in range(1,seq+1):
    n = int(input("Digite o %i número: " %i))
    números.append(n)
    
for k in range(len(números)):
    a = números.count(k)
    for j in range(a-1):
        números.remove(k)
   
print(números)
