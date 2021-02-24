def recebermodo():
    global modo,txt
    d = ["d","descriptografar"]
    c = ["c","criptografar"]
    m = input("Você deseja criptografar ou descriptografar uma mensagem? ")
    while m not in d and m not in c:
        print("Opção inválida!")
        m = input("Você deseja criptografar ou descriptografar uma mensagem? ")
    if m in d:
        modo = 0
    if m in c:
        modo = 1
    txt = (input("Digite a sua mensagem: "))
def chave():
    global ch
    ch =int(input("Coloque o valor da chave desejada: (1-26) "))
def msg():
    global modo,txt,ch
    ltxt = []
    if modo == 1:
        for j in txt:
            ltxt.append(j)
        for i in range(len(ltxt)):
            if ord(ltxt[i]) >= ord("a") and ord(ltxt[i]) <= ord("z"):
                if ord(ltxt[i]) - ch < ord("a") and ltxt[i] != " ":
                    ltxt[i]= chr(((ord(ltxt[i])+26)-ch))
                elif ltxt[i] != " " and ltxt[i] != ",":
                    ltxt[i]= chr(ord(ltxt[i]) - ch)
            if ord(ltxt[i]) >= ord("A") and ord(ltxt[i]) <= ord("Z"):
                if ord(ltxt[i]) - ch < ord("A") and ltxt[i] != " ":
                    ltxt[i]= chr(((ord(ltxt[i])+26)-ch))
                elif ltxt[i] != " " and ltxt[i] != ",":
                    ltxt[i]= chr(ord(ltxt[i]) - ch)               
    if modo == 0:
        for j in txt:
            ltxt.append(j)
        for i in range(len(ltxt)):
            if ord(ltxt[i]) >= ord("a") and ord(ltxt[i]) <= ord("z"):
                if ord(ltxt[i]) + ch > ord("z") and ltxt[i] != " ":
                    ltxt[i]= chr(((ord(ltxt[i])-26)+ch))
                elif ltxt[i] != " " and ltxt[i] != ",":
                    ltxt[i]= chr(ord(ltxt[i]) + ch)
            if ord(ltxt[i]) >= ord("A") and ord(ltxt[i]) <= ord("Z"):
                if ord(ltxt[i]) + ch > ord("Z") and ltxt[i] != " ":
                    ltxt[i]= chr(((ord(ltxt[i])-26)+ch))
                elif ltxt[i] != " " and ltxt[i] != ",":
                    ltxt[i]= chr(ord(ltxt[i]) + ch)
    texto = ""
    for i in ltxt:
        texto += i
    print(texto)
def main():
    recebermodo()
    chave()
    msg()
main()