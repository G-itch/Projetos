Lista_carros =[
    {"Nome": "Fusca","Litros":7},
    {"Nome": "Fiesta","Litros":5},
    {"Nome": "Vectra","Litros":7},
    {"Nome": "Golf","Litros":8},
    {"Nome": "Mustang","Litros":8},
    ]
cont= 1
for i in Lista_carros:
    print(f"Veículo {cont}")
    print("Nome:",i["Nome"])
    print("Km por litro:",i["Litros"])
    print("")
    cont+=1
print("Relatório Final")
aux = 1
for j in Lista_carros:
    lim = 8 - len(j["Nome"])
    print(aux,"-",j["Nome"]," "*lim+"-",j["Litros"],"- %.1f"%(1000/j["Litros"]),"litros","- R$ %.1f" %(1000/j["Litros"]*2.25))
    aux +=1
econo= []
eco = 0
for k in Lista_carros:
    if k["Litros"] > eco:
        eco = k["Litros"]
for kj in Lista_carros:
    if kj["Litros"] == eco:
        econo.append(kj["Nome"])

if len(econo) == 1:
    print("O carro mais econômico é o",econo[0])
else:
    print("Os carros mais econômicos são: %s" %(str(econo).strip("[]")))
