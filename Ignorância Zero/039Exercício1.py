def valor(x,y):
    if x == y:
        return x
    print(x)
    return valor(x+1,y)

print(valor(1,5))