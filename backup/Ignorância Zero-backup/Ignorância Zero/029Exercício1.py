class notas:

    def restartFrom(self, start):
        self.start = start

    def get(self, start, end):
        self.start = start
        while self.start != end:
            yield self.start
            self.start += 1
# um dia eu aprendo a fazer isso em cima
talunos = []
notas = notas()
for i in range(1,11):
    print("Aluno %i"%i)
    snota = 0
    for j in notas.get(1,5):
        nota = int(input("Digite a %i nota: " %j))
        if nota > 10:
            print("Nota inválida")
            notas.restartFrom(j-1)
        else:
            snota += nota
            print(snota)
    snota/= 4 
    print("%.2f" %snota)
    talunos.append(snota)
print(talunos)
for k in range(len(talunos)):
    if talunos[k] >= 7:
       print("O aluno %i passou!"%(k+1)) 


    