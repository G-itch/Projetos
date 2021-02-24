import random

player_vida = 500

player_sp = 100

inimigo_vida = 50
inimigos= []
ia = 0
ataque = 0
ni = int(input("Digite o número de inimigos:"))

for i in range(ni):
    inimigos.append(inimigo_vida)

while player_vida > 0 and sum(inimigos) > 0 :
    ataque = 0
    print("Vida =",player_vida,"\n SP=", player_sp)
    print(inimigos)
    ação =int(input("Deseja atacar (1) ou curar (2): "))
    if ação == 1:
        ia = random.randrange(ni)
        while inimigos[ia] <= 0:
            ia = random.randrange(ni)
        atp = random.randint(10,15) 
        inimigos[ia] -= atp
        print("Você causou %i de dano ao inimigo %i!" %(atp,ia+1))
    for ai in range(len(inimigos)):
        if inimigos[ai] > 0:
            at = random.randrange(4)
            if at >= 1:
                print("O inimigo %i causou %i de dano!" %(ai+1,at))
            if at == 0 :
                print("O inimigo %i errou o ataque!" %(ai+1))
        ataque += at
    player_vida -= ataque
    if ação == 2:
        if player_sp >= 10:
            player_sp -= 10
            cura = random.randint(10,15)
            if player_vida + cura <= 500:
                player_vida += cura
            else:
                player_vida = 500
        else:
            print("Você não tem mana o suficiente!")
    if player_sp + 3 > 100:
        player_sp = 100
    elif player_sp < 100:
        player_sp += 3
    if inimigos[ia] < 0:
        inimigos [ia] = 0
    print(inimigos)
if player_vida > 0:
    print("Parabéns você ganhou!")

