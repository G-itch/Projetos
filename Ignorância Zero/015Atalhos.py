
n = int(input("Digite o número de pessoas: "))

cont = 0 
ver1= True
while cont < n :
    print("Pessoa",cont+1)
    dia = int(input("Digite o dia de nascimento da pessoa %i: " %(cont+1)))
    mes = int(input("Digite o mês de nascimento da pessoa %i: " %(cont+1)))
    ano = int(input("Digite o ano de nascimento da pessoa %i: " %(cont+1)))
    if mes > 12:
        ver1 = False
    if mes == 1 or mes == 3 or mes== 5 or mes==7 or mes==9 or mes==10 or mes==12:
        verd= 31
    if mes == 4 or mes == 6 or mes==8 or mes == 11:
        verd=30
    else:    
        if ano%4==0 and ano%100!=0 or ano%400==0 :
            verd=29
        else:
            verd=28
    if dia > verd:
        ver2 = False
    else:
        ver2 = True

    if ver1== False or ver2 == False:
        print("Data inexistente, tente novamente")
    else:
        idade = int(input("Digite a idade a ser completada da pessoa %i:" %(cont+1)))
        print("A pessoa %i fará %i anos no dia %i/%i/%i" %(cont+1,idade, dia, mes, ano + idade))
        cont += 1 
