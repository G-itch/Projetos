tur = int(input("Qual a quantidade de turmas? "))
turT = 0
i=1
if tur > 0:
    while i <= tur:
        alunos = int(input("Há quantos alunos na turma %i? " %i))
        if alunos > 40 or alunos < 0 :
            print("Número inválido de alunos, tente novamente")
            
        else:
            turT += alunos
            i += 1
    print("A média de alunos na escola é de %g" %(turT/tur))
else:
    print("Número inválido de turmas, tente novamente")
    
   