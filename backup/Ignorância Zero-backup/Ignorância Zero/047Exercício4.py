print("Jogo do crime")
lista_p = ["Telefonou para a vítima? ","Esteve no local do crime? ","Mora perto da vítima? ","Devia para a vítima? " ,"Já trabalhou para a vítima? "]
lista_rs = ["s","S","sim","Sim"]
lista_rn = ["n","N","não","Não"]
resp_p = []
cl =[ 
    [0,1,"Inocente"],
    [2,"Suspeita"],
    [3,4,"Cúmplice"],
    [5,"Assasino"]
]
for i in lista_p:
    p = input(i)
    if p in lista_rs:
        resp_p.append(1)
    if p in lista_rn:
        resp_p.append(0)

cont = resp_p.count(1)
for c in cl:
    if cont == c[0]:
        vere = c[1]
        if c[1] != str(c[1]):
            vere = c[2]
    if cont == c[1]:
        vere = c[2] 

print("Decidimos que vocé é",vere)
