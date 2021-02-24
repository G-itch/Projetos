notas = []
notat = 0
for i in range (1,5):
    nota = int(input("Digite a %i° nota: " %i))
    notas.append("%i° nota = %i" %(i, nota))
    notat += nota
notas.append("Média total = %g" %(notat/4))
print(notas)