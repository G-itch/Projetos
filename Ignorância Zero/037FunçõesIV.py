x = 10
def soma(x):
    x+=3
    return x
print(soma(x))    

def modificalista(a):
    a[0] += 10


a = [1,2,3,4]

modificalista(a)

print(a)