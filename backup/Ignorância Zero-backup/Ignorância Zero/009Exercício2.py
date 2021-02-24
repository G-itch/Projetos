area = int(input("Digite a área a ser pintada :"))
litros = (area/3)
litrosint = int(litros)
tinta = 18
preço = 80
lata = litros/tinta 
lataint = litros//tinta
if lata<= 1:
    lata = 1
    preçoT = lata * preço
if lata != lataint and lata> 1:
    lata = litros//tinta
    preçoT =  (lata+1) * preço 
if lata == lataint and lata > 1:
    lata = litros//tinta
    preçoT = (lata * preço)    

if litros < 18:
    print("Você precisará de",litrosint,"litros porém só vendemos latas de tinta de",tinta,"litros no valor de",preço,"reais")
    confirmar = input("Você deseja efetuar a compra?")
    print ("O valor é de",preçoT,"reais")
else: 
    print("Você precisará de",litrosint,"litros porém só vendemos latas de tinta de",tinta,"litros no valor de",preço,"reais")
    confirmar = input("Você deseja efetuar a compra?")
    print ("O valor é de",preçoT,"reais") 

