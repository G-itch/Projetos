# raise ValueError("spam")
"""class nCM:
    def __enter__(self):
        print("Entramos no bloco with")
    def __exit__(self,tipo,valor, traceback):
        print(tipo)
        print(valor)
        print(traceback)
    
with nCM() as nosso:
    raise ValueError("spam")"""

class DeuErro(Exception):
    def __str__(self):
        return "Deu erro"

# raise DeuErro

class DeuerroArquivo(Exception):
    def __init__(self,linha,arq):
        self.linha = linha
        self.arq = arq
    def putz(self):
        print("putz!!")
    def __str__(self):
        return f"Deu erro na linha \n{self.linha+1}\nno arquivo {self.arq}"

try:
    raise DeuerroArquivo(2,"arquivo.txt")
except DeuerroArquivo:
    print(DeuerroArquivo(2,"arquivo.txt"))

try:
    raise DeuerroArquivo(2,"arquivo.txt")
except DeuerroArquivo as E:
    E.putz()
    print(E)
