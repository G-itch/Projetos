import random
meul = list(range(1,61))
meu = []

for k in range(1,7):
    numm = random.choice(meul)
    meu.append(numm)
    meul.remove(numm)
meu.sort()


soma = 0
sorteado = []
sortquadra = []
cont = 0
contn = 0
while meu != sortquadra:
    
    megasenaqua = list(range(1,61)) 
    for kq in range(1,6):
        numquadra = random.choice(megasenaqua)
        sorteado.append(numquadra)
        megasenaqua.remove(numquadra)
    for contn in range(2):
        meuquadra = [] 
        for ver in range(5): 
            meuquadra.append(meu[contn+ver])
            if  meuquadra == sorteado:
                print("Finalmente")
        print(meuquadra)
    print(sorteado, meuquadra, meu)
    exit()
    cont +=1
    print(cont)