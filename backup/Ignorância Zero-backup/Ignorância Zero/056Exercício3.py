contato = {"Nome":"Enzo","Telefone":23454567,"Celular":998767608,"E-mail":"enfurtini@hotmail.com"}
def keys(dic):
    keys = []
    for i in dic:
        keys.append(i)
    return f"dict_keys({keys})"
print(keys(contato))