
def mult(arg):
    m = 1
    for i in arg:
        m *= i
    
    return m
n = None
num = []
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
            
print(mult(num))