x= open("arquivo.txt","w")
x.write("Ola\nmundo")
x.close()
with open("arquivo.txt") as meuarquivo:
    for linha in meuarquivo:
        print(linha)

class nContextManager:
    def imprime(self,mag):
        print(mag)
    def __enter__(self):
        print("Entrando no bloco with")
        return self
    def __exit__(self,tipo,valor,traceback):
        print(tipo)
        print(valor) 
        print(traceback)

with nContextManager() as teste:
    teste.imprime("Ola Mundo")
