a =[1,2,3,4,5]
while sum(a) > 0 :
    print(a)
    n = int(input("Escolha um índice de um elemento da lista: (0 até %i) " %(len(a)- 1)))
    b = []
    for i in range(len(a)):
        if i != n:
            b.append(a[i])
    a = b
#a.pop(n)
