a = [1,2,3,4,5]

ele = int(input("Digite o elemento a ser colocado: "))
pos = int(input("Digite a posição: (0 até %i) " %(len(a) -1)))
"""
b = []
for i in range(len(a)):
    if i == pos:
        b.append(ele)
    b.append(a[i])
a = b
"""
a.insert(pos,ele)
print(a)
