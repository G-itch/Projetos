xint, yint = input("Digite dois números inteiros: ").split()
xint, yint = [int(xint), int(yint)]
nf = float(input("Digite um número real"))

a = (xint*2) * (yint / 2)
b = (xint*3) + nf
c = nf**3

print(a,"\n",b,"\n",c,)