import pdb

def main():
    pdb.set_trace()
    n = int(input("Digite n:"))
    x = float(input("Digite as coodenadas x do ponto 1:"))
    y = float(input("Digite as coordenadas y do ponto 1:"))
    ponto_m = (x,y)
    for i in range(1,n):
        x= float(input(f"Digite as coordenadas x do ponto {i+1}"))
        y= float(input(f"Digite as coordenadas y do ponto {i+1}"))
        ponto = [x,y]
        if angulo(ponto[0],ponto[1]) < angulo(ponto_m[0],ponto_m[1]):
            ponto_m = ponto
        print(ponto_m)
def módulo(y):
    if y <0:
        y = -y
    return y
def arctan (x):
    k, arctan, n =1 , 0 ,0
    while módulo(((x**(k))/k)*((-1)**(n))) >= 0.001:
        arctan += ((x**(k))/k)*((-1)**(n))
        x += 2 
        n += 1
    return arctan
def angulo (x,y):
    if y>x:
        angulo = (3.14/2) - arctan(x/y)
    else:
        angulo = arctan(y/x)
    return angulo

if __name__ == "__main__":
    main()