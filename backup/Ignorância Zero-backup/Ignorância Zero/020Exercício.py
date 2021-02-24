print("Equação de 2 grau")
a = int(input("Digite o valor de a: "))

if a == 0: 
    None
else:
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c
    raizmais = (-b + delta**(1/2))/(2*a)
    raizmenos = (-b - delta**(1/2))/(2*a)
    if delta < 0 :
        print("A equação não possui raízes reais")
        exit()
    if delta == 0 :
        print("A equação possui apenas uma raiz, sendo ela %i" %(raizmais))
    if delta > 0 :
        print("A equação possui duas raízes")
        print("x1 =",raizmais)
        print("x2 =",raizmenos)
    