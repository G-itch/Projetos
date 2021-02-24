n = int(input("Digite o tamanho da sequência: "))

for i in range (n):
    print("Sequência %i: " %(i+1))
    n2 = int(input("Digite um número da sequência: "))
    soma= 0
    while(n2 != 0):
        if(n2%2 == 0):
            soma += n2
        n2 = int(input("Digite um número da sequência: "))

    print("A soma dos números pares da sequência %i é igual a %i" %(i+1,soma))

        
        
