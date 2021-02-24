class Meu_objeto(object):
    def __init__(self):
        self.nome = "Enzo"
        self.idade = "16"
        print("Construtor chamado com sucesso")
    def imprime(self):
        print(f"\033[1;32mOlá meu nome é {self.nome}, eu tenho {self.idade} anos e terei muito sucesso e felicidade na minha vida!!!")

Meu_objeto().imprime()

























