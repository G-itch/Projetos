class minha(object):
    def __init__(self):
        self.x = 0
        self.y = 0

m = minha()
m.x = 5
m.z = 1
print(m.z)

class pessoaS2animais:
    def __init__(self,nome,peso,cão):
        self.nome = nome
        self.peso = peso
        self.cão = cão
    def treinar(self):
        self.cão.daApatinha()
        self.cão.latir()

class Cachorro:
    def __init__(self,nome,cor):
        self.nome = nome
        self.cordepelo = cor
    def daApatinha(self):
        print(f"O {self.nome} deu a patinha")
    def latir(self):
        print(f"O {self.nome} latiu")

Rex = Cachorro("Rex","Marrom")
Enzo = pessoaS2animais("Enzo",50,Rex)
Enzo.treinar()

def mudanome(pessoa):
    pessoa.nome = "Wesley"

mudanome(Enzo)

print(Enzo.nome)