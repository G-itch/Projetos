def main():
    global matrizl
    matrizl = []
    verm = input("Deseja criar uma matriz? (S/N) ")
    while verm == "S":
        if verm == "S":
            matriz()
        print(matrizl)
        ver = input("Deseja trocar um valor na matriz? (S/N) ")
        while ver == "S":
            if ver == "S":
                trocarvalormatriz()
            print(matrizl)
            ver = input("Deseja trocar outro valor na matriz? (S/N) ")
        verm = input("Deseja criar outra matriz? (S/N) ")

def matriz():
    global matrizl , m, n
    m = int(input("Digite o número de linhas: "))
    n = int(input("Digite o número de colunas: "))
    m2 = m
    for i in range(n):
        m = m2
        lista1 = []
        for j in range(m):
            valor = int(input("Digite o valor para atribuir a matriz %i:%i: " %(i+1,j+1)))
            lista1.append(valor)
        matrizl.append(lista1)
    return matrizl

def trocarvalormatriz():
    global matrizl , m, n
    trocarl = int(input("Qual linha da matriz você deseja trocar? (1:{})".format(m)))
    trocarc = int(input("Qual coluna da matriz você deseja trocar? (1:{}) ".format(n)))
    trocar = int(input("Por qual valor você deseja trocar a linha {} e a coluna {}? ".format(trocarl,trocarc)))
    matrizl [trocarl-1] [trocarc-1] = trocar

main()