def escolha():
    try:
        x = int(input("Digite um número de 1 a 20:"))
        if not 1<= x <=20:
            raise ValueError
        else: 
            print(f"\033[1;32mBoa escolha! O número {x} é ótimo!")
    except:
        print("\033[1;31mEntrada inválida!")

escolha()