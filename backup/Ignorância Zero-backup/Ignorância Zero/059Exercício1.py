class Quadrado(object):
    def __init__(self,l):
        self.lado = l
    def mudar_valor(self,lado):
        self.lado = lado
        return self.lado 
    def retornar_lado(self):
        return f"O lado do quadrado é igual a {self.lado}"
    def área(self):
        return f"A área do quadrado é igual a {self.lado*self.lado}"
    
Q = Quadrado(12)
# Q.mudar_valor(16)

print(Q.retornar_lado())
print(Q.área())
