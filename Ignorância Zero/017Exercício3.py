elei =int(input("Há quantos eleitores no total: "))
cand1=0
cand2=0
cand3=0
i=1
while i<= elei:
    voto = int(input("O elitor %d vota no candidato 1,2 ou 3 ? " %(i)))
    i+=1
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    else:
        print("Número inválido tente novamente")
        i-=1
    


print("Canditado 1: %d votos  Candidato 2: %d votos Candidato 3: %d votos" %(cand1, cand2,cand3))
