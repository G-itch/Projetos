def v(num):
    Max = 0
    for i in num:
        if i > Max:
            Max = i
    return Max
def neg(*arg):
    num = []
    n = None
    while n != -1:
        n = float(input("Digite um número: "))
        if n == -1:
            c = input("Deseja continuar? (S/N)")
            if c == 'S':
                num.append(n)
                n = 0
            if c == 'N':
                break
        else:
            num.append(n)
    return num

print("%g" %(v(neg())))