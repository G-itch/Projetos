def Listadecomida():
    start = 0
    lista = []
    def incrementa(item):
        nonlocal lista,start
        lista.append(item)
        start += 1
        print(start,item)
    return incrementa


compras = Listadecomida()
compras("Maçã")
compras("Carne")
