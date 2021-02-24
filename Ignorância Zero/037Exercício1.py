matrizl = []
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