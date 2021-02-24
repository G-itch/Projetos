"""try:
    x = int(input("Digite um número: "))
except:
    print("Deu erro")
    x=0
finally:
    print(x)"""

try: 
    a = open("arquivo.txt","r")
    linha = a.readline()
    linha = linha.strip("!")
    a.close()
    a = open("arquivo.txt","w")
    a.write(linha)
except FileNotFoundError:
    print("Deu erro!")
    a = open("arquivo.txt","w")
    a.write("DEU ERRROO!!!")
finally:
    a.close()
