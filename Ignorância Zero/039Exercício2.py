def soma(x,y):
    if x == y:
        return x
    return soma(x+1,y) + x

print(soma(1,12))