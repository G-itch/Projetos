print("Aluno 1:")
maxalt = minalt = float(input("Digite a altura do aluno 1: "))
for i in range(2, 10+1):
    print("Aluno %i:" %i)
    alt = float(input("Digite a altura do aluno %i: "%i))
    if alt > maxalt:
        maxalt = alt
        idalunomax = i
    elif alt < minalt:
        minalt = alt
        idalunomin = i

print("O aluno %i é o mais baixo com %.2f metros de altura"%(idalunomin, minalt))
print("O aluno %i é o mais alto com %.2f metros de altura"%(idalunomax, maxalt))