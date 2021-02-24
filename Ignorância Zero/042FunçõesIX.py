
def entrada():
    global n,ver
    ver = True
    while ver:
        n = int(input("Digite um numero de quatro dígitos:"))
        ver1()
        
def ver1():
    global n,ver
    if n <1000 or n > 9999:
        ver = True
        print("Número inválido!")
    else:
        ver = False
def sorteio():
    import random
    global número_s
    número_s= random.randrange(1000,10000)
def verfificar():
    global número_s, n,listanúm,listan,listanúm
    nk = n//1000
    nc = (n-nk*1000)//100
    nd = (n-(nk*1000+nc*100))//10
    nu = n-(nk*1000+nc*100+nd*10)
    listan = [nk,nc,nd,nu]
    nk2 = número_s//1000
    nc2 = (número_s-nk2*1000)//100
    nd2 = (número_s-(nk2*1000+nc2*100))//10
    nu2 = número_s-(nk2*1000+nc2*100+nd2*10)
    listanúm= [nk2,nc2,nd2,nu2]
def dica():
    global n,número_s,listanúm,listan,listam
    ver = True
    listam = []
    for i in range(len(listan)):
        cont = 0
        for j in range(len(listanúm)):
            aux = 1
            if listan[i] == listanúm[j] and i == j:
                print("Fermi")
                ver = False
                listam.append("Fermi")
                aux = 0
            elif listan[i] == listanúm[j] and cont == 0 and listan[i] != listanúm[i] and aux == 1 :
                cont = 1
                print("Pico")
                ver = False
                listam.append("Pico")
    if ver: 
        print("Bagels")
        listam.append("Bagels")
def jogada():
    global n,ver
    ver = True
    while ver:
        n = int(input("Insira sua jogada:"))
        ver1()
    

def main():
    global número_s,n,listam
    entrada()
    sorteio()
    for i in range(1,11):
        verfificar()   
        dica()
        n2 = n
        jogada()
        if número_s == n:
            print("Parabéns, Você ganhou!")
            exit()
        print("{} palpite: {} -> {}".format(i,n2,str(listam).strip("[]")))
    print("Que pena você perdeu :(")
    print(número_s)


main()     
