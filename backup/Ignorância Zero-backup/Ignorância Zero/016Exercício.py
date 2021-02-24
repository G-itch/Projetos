seque=int(input("Digite o tamanho da sequéncia: "))
ant= int(input("Digite o 1 número: "))
cont=1
aux=0
SegMAX=1
Seg=1
while cont < seque:

    próx= int(input("Digite o %i número: " %(cont + 1)))
    if próx>ant:
        Seg += 1
    if próx<ant:
        Seg = 1
    if Seg>SegMAX :
        SegMAX = Seg
    ant = próx
    cont+=1

print("A crescente máxima da sequência é",SegMAX)
    