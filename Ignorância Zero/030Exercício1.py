pessoas = []
idades = []
alturas = []

for i in range(1,6):
    print("Pessoa %i" %i)
    idade = int(input("Digite a idade:"))
    altura = float(input("Digite a altura:"))
    idades.append(idade)
    alturas.append(altura)
idades.reverse()
alturas.reverse()
for k in range(5):
    print("Pessoa %i: Idade: %i , Altura: %i" %(len(idades)-k, idades[k], alturas[k]))
    

