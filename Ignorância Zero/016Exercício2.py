seq= int(input("Digite o tamanho da sequência: "))
ant= int(input("Digite o 1 número: "))

cont=1
seg=1
segMax=1
while cont<seq:
    próx = int(input("Digite o %i número: " %(cont+1)))
    if próx != ant:
        seg += 1
    if seg>segMax:
        segMax = seg
    cont += 1
    ant=próx
print("A sua sequência tem tem",segMax,"segmentos de números iguais")
