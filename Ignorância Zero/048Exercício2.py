txt = input("Digite algo: ")
def alpha(txt):
    global letra
    letra = True
    for i in txt:
        if not("a"<= i <= "z" or "A" <= i <= "Z"):
            letra = False
            break
    return letra        
def mas():
    global txt,mas
    mas = False
    if alpha(txt):
        mas = True
        for j in txt:
            if j < "A" or j > "Z":
                mas = False
                break
    return mas
def minu():
    global txt,minu
    minu = False
    if alpha(txt):
        minu = True
        for j in txt:
            if  j < "a" or j > "z":
                minu = False
                break
    return minu
def main():
    alpha(txt)
    minu()
    mas()
    if letra:
        print("Só tem letra!")
    else:
        print("Não tem só letra!")
    if mas == True:
        print("Sò tem letra maiúscula!")
    if minu == True:
        print("Só tem letra minúscula!")

main()