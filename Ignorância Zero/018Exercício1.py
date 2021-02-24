seqini, seqfin = input("Digite o começo e o fim de uma tabuada: ").split()
seqini,seqfin= (int(seqini),int(seqfin))

for i in range(seqini,seqfin+1):
    print("Para o %i:" %(i))
    for j in range(1,seqfin+1):
        t = i*j
        print(i,"X",j,"=",t)
    print(" ")

