def sm(n1,n2):
    return n1+n2,n1*n2,n1/n2
a = int(input("Escreva um número: "))
b = int(input("Escreva outro número: "))
c,d,e = sm(a,b)
print(c,d,e)