x,y,z = input("Digite as três notas do aluno: ").split()
x,y,z = [float(x), float(y), float(z)]

média = (x + y + z)/3
if x > 10 or y > 10 or z > 10:
    print("Nota inválida tente novamente!")
else:
    if média == 10:
        print("O aluno foi aprovado com Distinção com %i de média" %(média)) 
    elif média >=7:
        print("O aluno foi aprovado com %i de média" %(média))
    elif média < 7:
        print("O aluno foi reprovado com %i de média" %(média))
