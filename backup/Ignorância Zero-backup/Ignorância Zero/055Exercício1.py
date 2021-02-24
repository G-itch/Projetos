contatos = []
contatos_alf = []
alfabeto = []
ent = int(input("Quantos contatos você deseja adicionar?"))

for i in range(ent):
    print(f"CONTATO {i+1}")
    Nome = input(f"Digite o nome do contato: ")
    while Nome.isalpha() == False:
        print("Digite apenas letras!")
        Nome = input(f"Digite o nome do contato: ")
    Nome = Nome.lower().capitalize()
    alfabeto.append(Nome)
    Telefone = int(input(f"Digite o telefone do contato: "))
    Celular = int(input("Digite o celular do contato: "))
    contato = {"Nome":Nome,"Telefone":Telefone,"Celular":Celular}
    contatos.append(contato) 
alfabeto.sort()
for j in alfabeto:
    for k in contatos:
        if j == k["Nome"]:
            contatos_alf.append(k)

for i in range(len(contatos_alf)):
    print("")
    print(f"Contato {i+1}")
    for j in contatos_alf[i]:
        print(j+":",contatos_alf[i][j])
    





 

