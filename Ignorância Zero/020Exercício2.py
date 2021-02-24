alt, sex= float(input("Qual a sua altura? ")) ,str(input("Qual seu sexo? masculino ou feminino: ")) 

if sex == ("masculino"):
    pesoideal = (72.7*alt) - 58
if sex == ("feminino"):
    pesoideal = (62.1*alt) - 44.7

peso = float(input("Qual é o seu peso?"))

if peso > pesoideal :
    print("Você está acima do peso em",round(peso - pesoideal, 2),"Kg")
    print("O seu peso ideal é de",round(pesoideal, 2),"Kg")
if peso == pesoideal :
    print("Você está com o peso ideal de",round(pesoideal, 2),"Kg")
if peso < pesoideal :
    print("Você está abaixo do peso em",round(pesoideal - peso, 2),"Kg")
    print("O seu peso ideal é de",round(pesoideal, 2),"Kg")
    

