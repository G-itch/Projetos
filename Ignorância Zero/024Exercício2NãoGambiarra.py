import random
print("Vamos jogar um jogo!")
porta = int(input("Escolha uma porta [1] [2] [3]: "))
prêmio = random.randrange(1, 4)
pf1 = list(range(1, 4))
pf1.remove(prêmio)
print(pf1)
portafalsa1 = random.choice(pf1)
pf1.remove(portafalsa1)
portafalsa2 = random.choice(pf1)
if prêmio == porta:
    nada = random.choice([portafalsa1,portafalsa2])
    print("Na porta %i não tem nada"%nada)
if portafalsa1 == porta:
    nada = portafalsa2
    print("Na porta %i não tem nada"%nada)
if portafalsa2 == porta:
    nada = portafalsa1
    print("Na porta %i não tem nada"%nada)
troca = input("Deseja trocar de porta? (S/N) ")
if troca == "S":
    tv = list(range(1,4))
    tv.remove(nada and porta)
    porta = random.choice(tv)
if prêmio == porta:
    print("Você ganhou!")
else:
    print("Você perdeu :(")



