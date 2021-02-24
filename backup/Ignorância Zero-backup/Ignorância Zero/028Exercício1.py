lista = []
n= 0
cont = 0
while n != -1:
    n = int(input("Digite um número inteiro:"))
    lista.append(n)
element = int(input("Escolha um elemento:"))


print("O número %i apareceu %i vezes" %(element, lista.count(element) ))

    
