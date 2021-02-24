import random
print("Olá, bem-vindo ao jogo")
porta = int(input("Escolha uma porta [1] [2] [3]:"))
prêmio = random.randint(1,3)
valorpfalso = list(range(1,4))
porta_falsa1 = random.choice(valorpfalso)
if porta_falsa1 + prêmio == 3:
    porta_falsa2 = 3
if porta_falsa1 + prêmio == 4:
    porta_falsa2 = 2
if porta_falsa1 + prêmio == 5:
    porta_falsa2 = 1
valores_permitidos = list(range(1, 4))
valores_permitidos.remove(prêmio and porta)
if porta_falsa1 == porta:
    bode = porta_falsa2
    print("Na porta %i tem um bode" %bode)
if porta_falsa2 == porta:
    bode = porta_falsa1
    print("Na porta %i tem um bode" %bode)
if prêmio == porta:
    bode = random.choice([porta_falsa1, porta_falsa2])
    print("Na porta %i tem um bode" %bode)
troca = input("Deseja trocar? (S/N)")
if troca == "S":
    if bode == 1 and porta == 2:
        porta = 3
    if bode == 1 and porta == 3:
        porta = 2
    if bode == 2 and porta == 1:
        porta = 3
    if bode == 3 and porta == 1:
        porta = 2
    if bode == 3 and porta == 2:
        porta = 1
    if bode == 2 and porta == 3:
        porta = 1
if porta == prêmio:
    print("Você ganhou!")
else:
    print("Você perdeu :(")

