class Banco(object):
    soma = 0
    aux = soma
    __total = 10000
    taxareserva = 0.2
    def calculareserva(self,soma= soma ):
        reserva = (self.__total+soma)*self.taxareserva
        Banco.__reserva = reserva
    def Fempréstimo(self,valor):
        if self.__reserva < self.__total+self.soma-valor:
            return True 
        else:
            return False
    def imprime(self):
        print(Banco.__total)
        print(Banco.aux)
class Conta(object):
    def __init__(self,saldo,ID,senha):
        self.__saldo = saldo
        self.__ID = ID
        self.__senha = senha
        Banco.soma += saldo
        Banco.calculareserva(Banco,Banco.soma)
    def depósito(self,senha,valor):
        while senha != self.__senha:
            print("\033[31 mSenha errada! Tente novamente!")
            senha = int(input("\033[32mDigite a senha: "))
        self.__saldo += valor
        Banco.soma += valor
        Banco.calculareserva(Banco,Banco.soma)
    def saque(self,senha,valor):
        while senha != self.__senha:
            print("\033[31 mSenha errada! Tente novamente!")
            senha = int(input("\033[32mDigite a senha: "))
        self.__saldo -= valor
        Banco.soma -= valor
        Banco.calculareserva(Banco,Banco.soma)
    def Pempréstimo(self,valor):
        if Banco.Fempréstimo(Banco,valor):
            print("\033[32mVocê pode fazer esse empréstimo")
        else:
            print("\033[31mVocê não pode fazer esse empréstimo")
itau = Conta(5000,123,1234)
itau.Pempréstimo(12000)