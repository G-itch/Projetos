def get2(dic,chave,valor = "O dicionário ainda não possuí algo relacionado a isso"):
    if chave in dic:
        return dic[chave]
    else:
        return valor
dicionário = {"Nome":"Enzo","Telefone":23454567,"Celular":998767608,"E-mail":"enfurtini@hotmail.com"}
print(get2(dicionário,"Endereço"))
