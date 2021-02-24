pessoa = {"nome":"Lucas", "Emprego":"Advogado", "idade":20, "cor do cabelo": "Preto"}
pessoa["nome"] = "João"
pessoa["peso"] = 50

class pessoa_:
    pass

enzo = pessoa_()
enzo.nome = "Enzo"
enzo.altura = 1.90
enzo.cordocabelo = "Preto"
print(enzo.__dict__)

pessoa = dict(nome="Lucas")
class person:
    def __init__(self, nome, idade , emprego):
        self.nome = nome
        self.idade = idade
        self.emprego = emprego
    def olá(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} e trabalho como {self.emprego}")

enzo = person("Enzo", 16, "programador")
enzo.olá()
print(enzo.__dict__)