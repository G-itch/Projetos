class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def imprimir(self):
        print(f"X = {self.x}, Y = {self.y}")

class Retângulo:
    def __init__(self,l,a,ponto):
        self.largura = l
        self.altura = a
        self.ponto = ponto
    def centro(self):
        self.ponto.x = self.largura/2
        self.ponto.y = self.altura/2
        self.ponto.imprimir()
p = Ponto(x=3,y=2)
r = Retângulo(17,6,p)
r.centro()


def mudar(rr):
    rr.largura = int(input("X: "))
    rr.altura = int(input("Y: "))
def centro(rr):
    rr.centro()

def menu(RR):
    res = input("Deseja mudar ou imprimir o centro do retângulo:")
    if res == "mudar":
        mudar(RR)
    elif res == "imprimir":
        centro(RR)
    else: 
        print("Opcão inválida!")
        menu(RR)
    centro(RR)
menu(r)



