números = []
númerosam = []
n = 0
cont = 0
while n != -1:
    cont += 1
    n = int(input("Digite o %i elemento: " %cont))
    if n == -1:
        pass
    else:
        números.append(n)

print(len(números), números,)
números.reverse()
for k in range(len(números)):
    print(números[k])

print(sum(números))
m =sum(números)/len(números)
print(m)
for i in range(len(números)):
    if números [i] > m:
        númerosam.append(números[i])
print(númerosam)
print(len(númerosam))
n7 = []
for i in range(len(números)):
    if números[i] < 7:
        n7.append(números[i])
print(n7)
print(len(n7))
print("Muito Obrigado canal Ignorância Zero!")