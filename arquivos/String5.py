txt = input("Digite seu nome: ")

def escada(x=0):
    global txt
    y = len(txt) - x
    if y == -2:
        exit()
    else:
        for i in range(len(txt)-1,y,-1):
            print(txt[i], end="")
        print("")
        return escada(x + 1)

print(escada())