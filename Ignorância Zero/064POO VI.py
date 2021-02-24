class Conta:
    def __init__(self,ID,saldo):
        """Cria a conta"""
        self.saldo = saldo
        self.ID = ID
    def __str__(self):
        return f"ID = {self.ID}\nSaldo = {self.saldo}"
    def __add__(self,outro):
        self.saldo += outro.saldo
    def __call__(self):
        print("ee")
r = Conta(1323,500)

print(r)

# r+50

print(r)

d = Conta(1234,500)

r + d
print(r)

print(r.__init__.__doc__)
r()
class Pai:
    pass

class Filha(Pai):
    pass

class Neta(Filha):
    pass

print(issubclass(Pai,Pai))

print(Neta.__bases__)

print(callable(Pai))