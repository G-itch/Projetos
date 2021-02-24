import random 

def n_ímpar():
    lista_n = []
    lista_i = []
    for i in range(50):
        n = random.randrange(1000)
        lista_n.append(n)
    for j in lista_n:
        if j%2 == 0:
            continue
        lista_i.append(j)
    print(lista_n)
    print(lista_i)

n_ímpar()