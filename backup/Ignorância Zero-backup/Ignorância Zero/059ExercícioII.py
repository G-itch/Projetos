class Retângulo(object):
    def __init__(self,A,B):
        self.ladoA = A
        self.ladoB = B
    def Mudar_valor(self,A,B):
        self.ladoA = A
        self.ladoB = B
    def retornar(self):
        return f"O comprimento do retângulo é igual a {self.ladoA} e a largura é igual a {self.ladoB}",self.ladoA,self.ladoB
    def Área(self):
        return f"A área do retângulo é igual a {self.ladoA*self.ladoB}"
    def Perímetro(self):
        return f"O perímetro do retângulo é igual a {(self.ladoA*2)*(self.ladoB*2)}"
def criar_local():
    global R
    com = float(input("Informe o comprimento do local: ")) 
    lar = float(input("Informe a largura do local: ")) 
    class local(object):
        def __init__(self):
            self.ladoA = com
            self.ladoB = lar
    L = local()
    if L.ladoA % R.ladoA == 0:
        A = L.ladoA / R.ladoA
    else:
        A = L.ladoA // R.ladoA + 1
    
    if L.ladoB % R.ladoB == 0:
        B = L.ladoB / R.ladoB
    else:
        B = L.ladoB // R.ladoB + 1
    

    return f"A quantidade de pisos necessários para preencher o local é de {int(A*B)} "
AA = float(input("Informe o comprimento do retângulo: "))
BB = float(input("Informe a largura do retângulo: "))
R = Retângulo(AA,BB)
print(R.Área())
print(criar_local())
    