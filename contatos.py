contatos_nomes = []
nomes =["joão","Maria"]

contatos = [
    {"nome" : "joão","idade": 21},
    {"nome" : "Maria","idade": 21},
    {"nome" : "josé","idade": 19}
]
for i in nomes:
    for j in contatos:
        if i == j ["nome"]:
            contatos_nomes.append(j)
for k in contatos_nomes:
    print(k ['nome'], k ['idade'])