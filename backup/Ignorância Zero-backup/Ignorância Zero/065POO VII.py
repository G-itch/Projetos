class Conta:
    def __init__(self,ID,saldo):
        """Cria a conta"""
        self.saldo = saldo
        self.ID = ID
        self.i = 7
    i = 5
    def depósito(self,valor):
        self.saldo += valor
    def saque(self, valor):
        self.saldo -= valor
    def __str__(self):
        return f"ID = {self.ID}\nSaldo = {self.saldo}"
    def __add__(self,outro):
        self.saldo += outro.saldo
    def __call__(self):
        print("ee")
    def __le__(self,outro):
        if self.ID <= outro.ID:
            return True
        return False
    def __eq__(self, outro):
        if self.ID == outro.ID:
            return True
        return False
    def __ge__(self,outro):
        if self.ID >= outro.ID:
            return True 
        return False
    def __lt__(self,outro):
        if self.ID < outro.ID:
            return True 
        return False
    def __nt__(self,outro):
        if self.ID != outro.ID:
            return True 
        return False
    def __gt__(self,outro):
        if self.ID > outro.ID:
            return True 
        return False
    def ff(self):
        print(self)
    
    ff(i)

class Contas(list):
    def sort(self):
        copia = self.copy()
        tam = len(self)
        self.clear()
        while len(self) < tam:
            min_id = copia[0]
            for i in copia:
                if i.ID < min_id.ID:
                    min_id = i
            self.append(min_id)
            copia.remove(min_id)      
            
           
class Banco:
    def __init__(self):
        self.contas = Contas()

Caixa = Conta(123,2000)

santander = Conta(12,34400)

Itau = Conta(456,3000)
Itau
Bradesco = Conta(11,2345)
Banco = Banco()
Banco.contas.append(Itau)
Banco.contas.append(Caixa)
Banco.contas.append(santander)
Banco.contas.append(Bradesco)





Banco.contas.sort()

print(Banco.contas[0])


print(Banco.contas[1])
print(Banco.contas[2])

print(Banco.contas[3])

