import random
teste = int(input("Digite o número de testes:"))

trocar = 0
n_trocar = 0
for i in range(1 ,teste + 1):
    porta = random.randrange(1,4)
    prêmio = random.randint(1,3)

    if porta == prêmio:
        n_trocar += 1
    else:
        trocar += 1

print("È vantajoso trocar em %.2f%% das vezes" %(trocar*100/teste))

print(print("È vantajoso não trocar em %.2f%% das vezes" %(n_trocar*100/teste)))