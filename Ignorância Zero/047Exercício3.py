
nome = input("Digite o seu nome de usuário: ")
senha = input("Digite a sua senha: ")
ver= False
for i in range(len(nome)):
    if nome[i] == senha[i] or ord(senha[i])- ord(nome[i]) == 32 or ord(senha[i])- ord(nome[i]) == -32:
        ver = True
    if nome[i] != senha[i] and ord(senha[i])- ord(nome[i]) != 32 and ord(senha[i])- ord(nome[i]) != -32:
        ver = False
        break
while ver == True:
    print("Senha inválida! Tente novamente. ")
    senha = input("Digite a sua senha: ")
    for i in range(len(nome)):
        if nome[i] == senha[i] or ord(senha[i])- ord(nome[i]) == 32 or ord(senha[i])- ord(nome[i]) == -32:
            ver = True
        if nome[i] != senha[i] and ord(senha[i])- ord(nome[i]) != 32 and ord(senha[i])- ord(nome[i]) != -32:
            ver = False
            break
