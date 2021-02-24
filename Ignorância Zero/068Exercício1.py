class Valorrepetido(Exception):
    def __init__(self,x):
        self.num = x
    def __str__(self):
        return(f"\033[1;31mO valor colocado está sendo repetido! O número {self.num} já está na lista!")

def main():
    lista = []

    for i in range(3):
        while True:
            try:    
                x = int(input("\033[094mEscolha um número:"))
                break
            except ValueError:
                print("\033[31mDigite apenas números!")
        if x not in lista:
            lista.append(x)
        else:
            raise Valorrepetido(x)




if __name__ == '__main__':
    main()