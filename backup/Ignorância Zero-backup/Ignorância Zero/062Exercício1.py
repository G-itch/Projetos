class ObjetoGráfico:
    def __init__(self,cor_de_preenchimento,preenchido,cor_de_contorno):
        self.corp = cor_de_preenchimento
        self.preenchido = preenchido
        self.corc = cor_de_contorno
    def corpreenchida(self):
        print(f"O objeto está com a cor de preenchimento {self.corp}.")
    def preenchimento(self):
        if self.preenchido.lower()[0] == "s":
            print("O objeto está preenchido")
            return
        print("O objeto não está preenchido")
    def contorno(self):
        print(f"O objeto está contornado com a cor {self.corc}")
    def área(self):
        pass
    def perímetro(self):
        pass

class retângulo(ObjetoGráfico):
    def __init__(self,base,altura,cor_de_preenchimento,preenchido,cor_de_contorno):
        super(retângulo,self).__init__(cor_de_preenchimento,preenchido,cor_de_contorno)
        self.base = base
        self.altura = altura
        if self.base == self.altura:
            self.nome = "quadrado"
        else:
            self.nome = "retângulo"
    def área(self):
        print(f"A área do {self.nome} é igual a {self.base*self.altura}")
    def perímetro(self):
        print(f"O perímetro do {self.nome} é igual a {self.base*2+self.altura*2}")

class Circulo(ObjetoGráfico):
    def __init__(self,raio,cor_de_preenchimento,preenchido,cor_de_contorno):
        super(Circulo,self).__init__(cor_de_preenchimento,preenchido,cor_de_contorno)
        self.raio = raio
        self.nome = "Circulo"
    def área(self):
        import math
        print("A área do {} é igual a {:.2f}".format(self.nome,math.pi*self.raio))
    def perímetro(self):
        import math
        print("O perímetro do {} é igual a {:.2f}".format(self.nome,math.pi*2*self.raio))
class Triângulo(ObjetoGráfico):
    def __init__(self,base,altura,cor_de_preenchimento,preenchido,cor_de_contorno):
        super(Triângulo,self).__init__(cor_de_preenchimento,preenchido,cor_de_contorno)
        self.base = base
        self.altura = altura
        self.nome = "triângulo"
    def área(self):
        print(f"A área do {self.nome} é igual a {(self.base*self.altura)/2}")
    def perímetro(self):
        print(f"O perímetro do {self.nome} é igual a {(((self.base/2)**2+self.altura**2)**0.5)*2+self.base}")

t = Triângulo(6,4,"vermelho","Sim","laranja")
t.perímetro()
c = Circulo(5,"Amarelo","Não","Rosa")
c.perímetro() 
c.área() 

         