def soma(num):
    s = 0
    for i in range(len(num)):
        s += num[i]
    return s

num = []
n = None
while n != -1:
    n = float(input("Digite um número: "))
    num.append(n)
print("A soma dos valores é igual a %g" %(soma(num)))

