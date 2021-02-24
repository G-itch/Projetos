ns = []
n10 = []
n = None
cont = 0
while n != -1:
    cont +=1
    n = int(input("Digite o %i número: "%cont))
    ns.append(n)

for k in range(len(ns)):
    if ns[k] >10:
        n10.append(ns[k])

print("Os números maiores que 10 são:",str(n10).strip('[]'))
