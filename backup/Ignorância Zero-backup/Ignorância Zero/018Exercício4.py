m = int(input("Digite um número: "))
números = []
cont = 0
for n in range(1, m+1):
    cont += n
i = cont * 2 - m
res = i * m
i -= m
i +=1
for jk in range(m):
    números.append(i)
    i +=2
print(m," ao cubo resulta em",res,"que é a soma de:",str(números).strip('[]'))









