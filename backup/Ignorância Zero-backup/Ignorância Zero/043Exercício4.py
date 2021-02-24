import random 
n = random.randrange(1,101)
print("Tente adivinhar o número que eu estou pensando!(De 1 a 100)")
nc = int(input("Chute um número: "))
while nc > 100:
    print("Número inválido! Tente novamente ")
    nc = int(input("Chute um número: "))
ver = False
for i in range(2,11):
    if nc == n:
        ver = True
        break
    elif nc < n:
        print("Chute mais alto!")
    elif nc > n:
        print("Chute mais baixo!")
    nc = int(input("Seu {} chute: ".format(i)))
    print("{} de 10".format(i) )

if ver:
    print("Parabéns! Você ganhou!")
    print("Você Chutou {} vezes.".format(i))
else:
    print("Você perdeu :(")