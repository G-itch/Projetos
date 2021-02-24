"""
x = 10

del x

l = [1,2,3]

del l[2]

print(l)

d = {"1":1,"2":2,"3":3}

del d['1']

print(d)
"""
class pessoa(object):
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade
    def nomei(self):
        print(f"Olá eu sou o {self.nome}")
Enzo = pessoa("Enzo","23")
print(Enzo.__init__("Enzo",17))
Enzo.nomei()

# 

print([1,2,3] is [1,2,3])
l = [1,2,3]
l2 = l
print(l is l2)
