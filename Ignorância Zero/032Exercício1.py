import random
meul = list(range(1,61))
meu = []

for k in range(1,6):
    numm = random.choice(meul)
    meu.append(numm)
    meul.remove(numm)
meu.sort()


soma = 0
sorteado = []
sortquadra = []
cont = 0



while meu != sorteado:
    megasena = list(range(1,61))
    for j in range(1,7):
        num = random.choice(megasena)
        sorteado.append(num)
        megasena.remove(num)
    cont +=1
    print(cont)
soma += cont



