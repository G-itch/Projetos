import random
matriz = []
def matrizrandom():
    global random, matriz
    ns = list(range(16))
    for i in range(4):
        aux = []
        for j in range(4):
            n = random.choice(ns)
            aux.append(f'[{n:^5}]')
            ns.remove(n)
        matriz.append(aux)
    for k in range(i+1):
        for kj in range(j+1):
            print(matriz[k][kj], end = "")
        print()


matrizrandom()