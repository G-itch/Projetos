txt = input("Digite seu nome: ")

def escada(x=0):
    global txt
    if x == len(txt)+1:
        exit()
    else:
        for i in range(x):
            print(txt[i], end="")
        print("")
        return escada(x + 1)

print(escada())