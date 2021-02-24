import random
FIMG =[[0,'''

  +---+
  |   |
      |
      |
      |
      |
========='''],
[1,'''

  +---+
  |   |
  O   |
      |
      |
      |
========='''],
[2,'''

  +---+
  |   |
  O   |
  |   |
      |
      |
========='''],
[3,'''

  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''],
[4,'''

  +---+
  |   |
  O   |
 /|\\  |
      |
      |
========='''],
[5,'''

  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
========='''],
[6,'''

  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']] 

lista_palavras = "Mesa Sofá Computador Maçã Óculos Camisa Calça Bermuda Formiga Cadeira Gato Cachorro Zoológico".lower().split()

def palavraescolhida():
    global lista_palavras,palavra,lista
    lista = []
    palavra = random.choice(lista_palavras)
    for i in palavra:
        lista.append(i)

def palavraescondida():
    global palavra,paes,lista_paes,pk
    lista_paes = []
    paes = ""
    for i in palavra:
        lista_paes.append("_")
        pk = i
def palpite():
    global lista_paes,lista,pl_e,cont
    cont = 0
    pl_e = [] 
    p = input("Adivinhe uma letra: ")
    while p.isalpha() == False or len(p) != 1:
        print("Caracter inválido!") 
        p = input("Adivinhe uma letra: ")
    while p in lista_paes or p in fl_e:
        print("Você já chutou essa letra!")
        p = input("Adivinhe uma letra: ")
    if p in lista:
        for j in range(len(lista)):
            if lista[j] == p:
                lista_paes[j] = p
    else:
        pl_e.append(p)
        cont += 1
fl_e = ""
def formatação():
    global lista_paes,pl_e,palavraver,form,fl_e,rl_e
    form = ""
    rl_e = ""
    palavraver = ""
    for i in lista_paes:
        form += (i+" ")
        palavraver+= i
    for j in pl_e:
        fl_e += j
    for k in fl_e:
        rl_e += (k + " ")
def main():
    global FIMG,cont,form,fl_e,palavraver,palavra,rl_e
    palavraescolhida()
    palavraescondida()
    print("F O R C A")
    print(FIMG[0][1])
    print("Letras erradas:")
    print("_ "*len(lista_paes))
    palpite()
    formatação()
    while len(fl_e) != 6:
        for j in FIMG:
            if len(fl_e) == j[0]:
                print(j[1])
        print("Letras erradas:",rl_e)
        print(form)
        palpite()
        formatação()
        if palavraver == palavra:
            formatação()
            print(form)
            print(f"A palavra era {palavra}")
            print("Parabéns você ganhou!")
            jogar()
    print(FIMG[6][1])
    print(f"Você perdeu, a palavra era {palavra}")
    jogar()

def jogar():
    global fl_e
    opções_s = ["s","S","sim","Sim"]
    opções_n =  ["n","N","não","Não"]
    j = input("Deseja jogar novamente?")
    while j not in opções_s and j not in opções_n:
        print("Opção inválida")
        j = input("Deseja jogar novamente? ")
    if j in opções_s:
        print("Bom jogo!")
        fl_e = ""
        main()
    else:
        print("Até breve")
        exit()

main()