import random 
lista = []
n = int(input("Digite o número de vezes que será lançado o dado: "))
for i in range(n):
    lista.append(random.randrange(1,7))
    

for j in range(1,7):
    print("A face número %i foi tirada %i vezes (%.4g%%)" %(j ,lista.count(j), 100*lista.count(j)/n))

 