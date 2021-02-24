lsal = []
lab = []
abt = 0
cont = 0
sal = float(input("Digite o salário do funcionário: "))

while sal != 0 :
    while sal < 0:
        print("Número inválido! Tente novamente!")
        sal = float(input("Digite o salário do funcionário: "))
    ab = (sal / 100) * 20
    if ab <100:
        ab = 100
        cont += 1
    lsal.append(str(sal))
    lab.append(str("%.1f"%ab))
    abt += ab
    sal = float(input("Digite o salário do funcionário: "))
print("")
print("   Salário   -    Abono   ")
for i in range(len(lsal)):
    lims = 8 - len(lsal[i]) 
    lima = 8 - len(lab[i])
    print("R$"," "*lims,lsal[i],"- R$"," "*lima, lab[i])
print("")
if len(lsal) == 1:
    print("foi processado {} colaborador".format(len(lsal)))
else:
    print("Foram processados {} colaboradores".format(len(lsal)))
print("Total gasto em abono: R$ {}".format(abt))

txt = "Valor mínimo pago a {} colaborador" 
if cont > 1:
    txt += "es"
if cont != 0:
    print(txt.format(cont))

mv = 0
for j in lab:
    if float(j) > mv:
        mv = float(j)
print("Maior valor de abono pago: R$ {}".format(mv))