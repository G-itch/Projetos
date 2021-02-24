ver = True
turnos = [["m","M","manhã","Manhã","Bom dia!"],["v","V","Tarde","tarde","Boa tarde!"],["n","N","noite","Noite","Boa noite!"]]
t = input("Em que turno você estuda? ")
for i in turnos:
    if t in i:
        ver = False
while ver == True:
    print("Opção Inválida!")
    t = input("Em que turno você estuda? ")
    for i in turnos:
        if t in i:
            ver = False
for j in turnos:
    if t in j:
        h = j[4]
print(h)
