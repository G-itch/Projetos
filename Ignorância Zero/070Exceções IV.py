"""try:
    num = 1/0
    int(num)
except Exception as E:
    raise ValueError from E"""

while True:
    try:
        x = int(input("\033[32mDigite um número de 1 a 20: "))
    except ValueError :
        print("\033[31mDigite apenas números!")
    except: 
        print("\033[31mEntrada inválida!")
    else:
        break

test =True

if not 1<=x<=20:
    test =False

assert test,x

if __debug__:
    if not test:
        raise AssertionError(x)

def raiz(x):
    assert x > 0 , "Tenha certeza que o número é maior que 0"
    return x ** 1/2

raiz(-2)