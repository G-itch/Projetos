print("Digite um número maior que 0 e menor que 1000.")
num = int(input("Qual o número?"))

cem=100
dez=10
um=1
c= num//cem
d= (num%cem)//dez
u= ((num%cem)% dez)//um
ce= "centena"
de= "dezena"
uni= "unidade"

if c > 1 and  d >= 1 and u >=1:
    ce = ce + "s,"
elif d >= 1 and u >=1:
    ce = ce + ","
elif c> 1 and (d == 0 and u >= 1) or (d>=1 and u==0):
    ce = ce + "s e"
elif (d == 0 and u >= 1) or (d>=1 and u==0):
    ce = ce + " e"
elif c > 1 :
    ce = ce +"s"


if  d> 1 and u >= 1 :
    de = de + "s e"
elif u >= 1:
    de = de + "e"
elif d > 1 :
    de = de + "s"

if u > 1 :
    uni = uni + "s"



if num<=0 or num>=1000:
    print("Número inválido")
elif c>=1 and d>=1 and u>=1:
    print(c,ce,d,de,u,uni)    
elif c==0 and d>=1 and u>=1:
    print(d,de,u,uni)
elif c>=1 and d==0 and u>=1:
    print(c,ce,u,uni)
elif c==0 and d==0 and u>=1:
    print(u,uni)
elif c>=1 and d>=1 and u==0:
    print(c,ce,d,de)
elif c>=1 and d==0 and u==0:
    print(c,ce)
elif c==0 and d>=1 and u==0:
    print(d,de)

