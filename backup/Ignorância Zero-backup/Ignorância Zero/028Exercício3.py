import random
votos = []
n = -1 
cont = 0
votoMax = 0
while n != 0:
    voto = int(input("Digite o número do jogador que deseja votar:"))
    if voto == 0:
        n = 0
    if 1 > voto or voto > 23:
        print("Número inválido, tente novamente!")
    else:
        votos.append(voto)
        cont+=1
for i in range(1,24):
    print("O jogador número %i recebeu %i votos\
    (%.4g%%)" %(i, votos.count(i),100*votos.count(i)/cont))
    if votos.count(i) > votoMax:
        iMax = i
        votoMax = votos.count(i)
print("O jogador número %i ganhou o título de melhor\
jogador da partida com %i votos (%.4g%%)" %(iMax,votoMax,100*votoMax/cont))


    