class mamifero(object):
    def __init__(self, cordepelo, gênero, andar):
        self.cordepelo = cordepelo
        self.gênero = gênero
        self.patas = andar
    def falar(self):
        print("Olá, eu sou um mamifero e eu sei falar")
    def andar(self):
        print("Estou andando sobre %i patas" %(self.patas))
    def amamentar(self):
        if self.gênero.lower()[0] == "m":
            print("Machos não amamentam")
            return
        print("Amamentando o meu filhote")

"""rex = mamifero("marrom","M",4)
rex.falar()
rex.andar()
rex.amamentar()

julia = mamifero("preto","F",2)
julia.falar()
julia.andar()
julia.amamentar()
"""
class pessoa(mamifero):
    def __init__(self,nome,cordepelo,gênero,andar):
        super(pessoa,self).__init__(cordepelo, gênero, andar)
        self.nome = nome
    def falar(self):
        print("Olá, eu sou uma pessoa!")
        super(pessoa,self).falar()
Roberta = pessoa("Roberta","loiro","F",2)
Roberta.falar()
Roberta.amamentar()
Roberta.andar()