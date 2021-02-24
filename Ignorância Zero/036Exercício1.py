
def criarconta():
    global contas,saldo
    ver = False
    while ver == False:
        c = float(input("Digite um número de 6 dígitos: "))
        while c < 100000 or c > 999999:
            print("Número inválido!")
            c = float(input("Digite um número de 6 dígitos: "))
        if contas == []:
            ver = True
        else:
            for r in contas:
                if r == c:
                    print("Conta já existente")
                    ver = False
                else:
                    ver = True
    contas.append(c)
    s = int(input("Digite o valor de depósito: "))
    while s <= 0:
        print("Depósito inválido!")
        s = int(input("Digite o valor de depósito: "))
    saldo.append(s)

def versaldo():
    global saldo
    vs = input("Deseja ver o saldo? (S/N) ")
    if vs == "S":
        print("Saldo total = {}".format(sum(saldo)))

def main():
    global contas,saldo
    contas = []
    saldo = []
    p = "Criar"
    while p == "Criar":
        p = input("Deseja Criar uma nova conta ou Fechar o programa: ")
        if p == "Criar":
            criarconta()
            versaldo()
    return contas, saldo
contas,saldo = main()
main()





    


