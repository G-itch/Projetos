try:
    lista = []
    lista.append(int('dsag'))
except IndexError:
    print("Erro")
except ValueError:
    print("Erro no valor")

try:
    lista = []
    lista.append(int('dsag'))
except (IndexError,ValueError) as Excessão:
    print(Excessão)
    print("Erro")
