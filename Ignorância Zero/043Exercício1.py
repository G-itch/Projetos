def criarlista():
    global lista,elementos
    lista = int(input("Digite o tamanho da lista: "))
    elementos = []
    for i in range(1,lista+1):
        n = float(input("Digite o elemento {} de {}:".format(i,lista)))
        elementos.append(n)
def somar():
    global lista,elementos,somat
    soma = int(input("Digite o número de elementos que deseja somar: "))
    somat = 0
    for j in range(lista):
        somat += elementos[j]
        if j+1 == soma:
            break


def main():
    global somat
    criarlista()
    somar()
    print("A soma é {}".format(somat))

main()