txt = input("digite algo: ")
def split(x):
    lista = []
    cont = 0
    ass = 0
    for i in range(len(x)):
        aux = ""
        if x[i] == " ":
            auxx = cont
            cont = i
            print(i)
            for j in range(auxx + ass,i):
                aux += x[j]
                ass = 1
            lista.append(aux)
    for k in range(len(x)-1,0,-1):
        if x[k] == " ":
            tr = k
            break
    aux = ""
    for kj in range(tr+1,len(x)):
        aux += x[kj]
    lista.append(aux)
    print(lista)

split(txt)
print(len(txt))