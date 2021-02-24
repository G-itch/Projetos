def conversor(n1,n2):
    if n1 > 24 or n2>59 or (n1 or n2 <0):
        n1 = -1
        n2 = -1
        conv = "Horário inválido!"
    elif n1 < 12 or n1 ==24:
        if n1 == 24:
            n1 = 0
        conv = "AM"
    elif n1 > 12 and n2 >=1:
        conv = "PM"
        for i in range(1,(n1+1)-12):
            n1 = i
    return (n1,n2,conv)
h = None
while h != -1:
    h = int(input("Digite a hora: "))
    m = int(input("Digite os minutos: "))
    a,b,c= conversor(h,m)
    if a == -1:
        print(c)
    else:
        print("%i:%i %s" %(a,b,c))
    

