class pessoa(object):
    global P
    def __init__(self,n,i,p,a):
        self.nome = n
        self.idade = i
        self.peso = p 
        self.altura = a
    def crescer(self,cm):
        self.altura += cm
        return self.altura
    def envelhecer(self,an):
        for i in range(1,an+1):
            if self.idade + i < 21:
                P.crescer(0.5)
        self.idade += i
        return self.idade 
    def engordar(self,kg):
        self.peso += kg
        return self.peso
    def emagrecer(self,kg):
        self.peso -= kg
        return self.peso   
    def show(self):
        print(self.nome,self.idade,self.peso,self.altura)
P= pessoa("Hugo",8,63,172)
P.envelhecer(5)
P.show()