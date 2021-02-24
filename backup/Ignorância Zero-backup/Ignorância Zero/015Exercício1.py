print("Verifique se um número é triangular")

n = int(input("Digite o número: "))

cont = 0
tri = 0
while tri < n:
    cont1 = cont + 1
    cont2 = cont + 2
    cont3 = cont + 3
    tri = cont1*cont2*cont3
    cont += 1
    

if tri == n:
    print("O valor ",tri,"é triangular, sendo multiplicado por",cont1,"X",cont2,"x",cont3)
else:
    print("O valor não é triangular")

    




