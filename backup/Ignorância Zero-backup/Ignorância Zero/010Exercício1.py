print("O saque disponível é entre 10 e 600 reais.")
saque = int(input("Qual o valor a ser sacado? "))
if saque<10 or saque>600:
    print("O valor solicitado está indisponível.")
else:
    print(saque,"reais")


n1= 100
n2= 50
n3= 10
n4= 5
n5= 1
n11= saque//n1
n22r= saque%n1
n22= n22r//n2
n33r= n22r%n2
n33= n33r//n3
n44r= n33r%n3
n44= n44r//n4
n55r= n44r%n4
n55= n55r//n5


print("O programa irá fornecer",n11,"notas de",n1,"reais,",n22,"notas de",n2,"reais,",n33,"notas de",n3,"reais,",n44,"notas de",n4,"reais e",n55,"notas de",n5,"reais.")


