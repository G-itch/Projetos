"""class ObjetoGráfico(object):
    def __init__(self,corp,p,corc):
        self.corp = corp
        self.p = p
        self.corc = corc
    def area(self):
        pass
    def perímetro(self):
        pass
    def info(self):
        print(f"{self.area()} metros² serão preenchidos com a cor {self.corp}")
"""
class Conta(object):
    __total = 10000
    reserva = 0.1
    def __init__(self,ID,saldo):
        self.__ID = ID
        self.saldo = saldo
        Conta.__total += self.saldo
    def depósito(self,valor):
        self.saldo += valor
        Conta.__total += valor
    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            Conta.__total -= valor
        Conta.__imprimereserva(self)
    def __imprimereserva(self):
        print(Conta.__total*Conta.reserva)
itau = Conta(123,5000)
itau.depósito(500)
itau.depósito(1000)
itau.saque(100)