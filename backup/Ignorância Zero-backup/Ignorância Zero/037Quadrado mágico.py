import random
from pynput.keyboard import Key,Controller 
keyboard = Controller()
def main():
    global verq,random,matriz
    matrizrandom()
    verq = False
    while verq == False:
        movimento()
        verificasevenceu()

matriz = []
def matrizrandom():
    global random, matriz
    ns = list(range(16))
    for i in range(4):
        aux = []
        for j in range(4):
            n = random.choice(ns)
            aux.append(n)
            ns.remove(n)
        matriz.append(aux)
    for k in range(i+1):
        for kj in range(j+1):
            print(f"[{matriz[k][kj]:^3}]",end="")
        print()
    print("-=" * 30)
def verificasevenceu():
    global matriz,verq
    matrizv = []
    cont = 0
    for j in range(4):
        aux = []
        for kj in range(4):
            cont +=1 
            if cont == 4*4:
                cont = 0
            aux.append(cont)
        matrizv.append(aux)
    if matrizv == matriz:
        print("VOCÊ GANHOUUUUU!!!!!!!")
        verq = True
def movimento():
    global matriz, keyboard
    movimentos = ["1-Esquerda","2-Direita","3-De cima","4-De baixo"]
    aux = []
    cont2 = 0
    for gh in range(4):
        cont = 0
        for hk in range(4):
            cont += 1
            cont2 += 1
            if matriz [gh] [hk] == 0:
                x, y = gh,hk
                x2,y2 = gh,hk
    if x == 0:
        movimentos.remove(movimentos[2])
    if x == 3:
        movimentos.remove(movimentos[3])
    if y == 0:
        movimentos.remove(movimentos[0])
    if y == 3:
        movimentos.remove(movimentos[1])
    move = int(input("Deseja mover a peça: {} : ".format(movimentos)))
    if move == 1:
        aux.append(matriz [x2] [y2])
        if y2 - 1 == -1 :
            print("+=" * 30)
            print("Movimento inválido!")
            print("+=" * 30)
        else:
            matriz [x2] [y2] = matriz [x2] [y2-1]
            matriz [x2] [y2-1] = int(str(aux).strip('[]'))
    if move == 2:
        aux.append(matriz [x2] [y2])
        if y2 + 1 == 4 :
            print("+=" * 30)
            print("Movimento inválido!")
            print("+=" * 30)
        else:
            matriz [x2] [y2] = int(matriz [x2] [y2+1])
            matriz [x2] [y2+1] = int(str(aux).strip('[]'))
    if move == 3:
        aux.append(matriz [x2] [y2])
        if x2 - 1 == -1 :
            print("+=" * 30)
            print("Movimento inválido!")
            print("+=" * 30)
        else:    
            matriz [x2] [y2] = matriz [x2-1] [y2]
            matriz [x2-1] [y2] = int(str(aux).strip('[]'))
    if move == 4:
        aux.append(matriz [x2] [y2])
        if x2 + 1 == 4 :
            print("+=" * 30)
            print("Movimento inválido!")
            print("+=" * 30)
        else:
            matriz [x2] [y2] = matriz [x2+1] [y2]
            matriz [x2+1] [y2] = int(str(aux).strip('[]'))
    for h in range(4):
        for o in range(4):
            print(f"[{matriz [h] [o]:^3}]", end = "")
        print()
    print("-=" *30)
main()