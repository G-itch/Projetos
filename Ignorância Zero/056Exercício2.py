contato = {"Nome":"Enzo","Telefone":23454567,"Celular":998767608,"E-mail":"enfurtini@hotmail.com"}
def items(dic):
    items = []
    for i in dic:
        tupla = (i,dic[i])
        items.append(tupla)
    dict_items= (f"dict_items({items})")
    return dict_items

print(items(contato))