"""def incrementa(x):
    x+=1
    return x
y=10

print(incrementa(y))

def x(y):
    a = 1
    y += a
    print(y)
#a não existe fora da função"""

X=10
def incrementa():
    global X # atribuí uma variável global a função
    incremento = 5 #variável local
    X +=incremento #cópia do valor de x
    return X
print(incrementa())



