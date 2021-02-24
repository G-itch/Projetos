p = int(input("Digite um número: "))
q = int(input("Digite um número maior ou igual ao o anterior: "))

aux_p=p
contdig = 0
aux_q = q
while aux_p != 0 :
    aux_p //=10
    contdig += 1

comparando = True

while comparando:
    subnum= aux_q %(10**contdig)
    if subnum == p:
        comparando = False
        print("O número",p,"é subnúmero de",q)
    
    aux_q //=10
    if aux_q == 0:
        comparando = False

if subnum != p:
    print("O número",p,"não é subnúmero de",q)
