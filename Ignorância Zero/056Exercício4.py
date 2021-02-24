contato = {"Nome":"Enzo","Telefone":23454567,"Celular":998767608,"E-mail":"enfurtini@hotmail.com"}
def values(dic):
    values = []
    for i in dic:
        values.append(dic[i])
    return f"dict_values({values})"
print(values(contato))
