p = int(input("Digite um número: "))
q = int(input("Digite outro número: "))

aux_n = 1
cont = 1
while p//aux_n >= 10:
    aux_n *= 10
    cont += 1
b = False
q2 = q
while q >= p:
    ver = q%10**(cont)
    if ver == p:
        b = True
        break
    q = q//10
    print(q)

    

if b:
    print("{} é subnúmero de {}".format(p,q2))
else:
    print("{} não é subnúmero de {}".format(p,q2))
