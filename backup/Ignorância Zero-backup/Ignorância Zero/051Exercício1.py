lista = []
soma = 0
média = 0
cont = 0
perc = []
# pega o conteúdo do arquivo
usuários = open("arquivos/051usuarios.txt","r")

def m(x):
    # tranforma o número de Bytes para Mega
    mega = float(x)/1e+6
    return mega
def per(x):
    # realiza a soma dos valores em Mega
    global soma
    soma += x
def per2(x):
    # faz a média de distribuição de espaço entre os usuários
    global média,lista
    média = x/len(lista)
x = usuários.readlines()
# armazena o nome dos usuários e dos valores que eles possuem em uma lista
for i in range(len(x)):
    linha = ""
    for j in range(len(x[i])):
        if x[i][j:j+2] != "\n":
            linha += x[i][j]
    lista.append(linha)
# realiza a leitura dos bytes (de forma a pegar da lista inteira o valor) e reliza as contas
for i in range(len(lista)):
    byte = ""
    for j in range(len(lista[i])):
        if j > 15:
            byte += lista[i][j]
    mega = m(byte)
    per(mega)
    perc.append(mega)
    meg = "%.2f"%(mega)
    # muda o valor antigo para o novo na lista
    lista[i] = (lista[i].replace(byte," "*(7-len(meg))+"%.2f"%(mega))+" MB")
per2(soma)
# vê a porcentagem de uso de cada usuário
for i in range(len(perc)):
    por = perc[i] /(soma/100) 
    por = ("%.2f %%"%por)
    lista[i] += (" "*(15-len(por))+por)
# formatação
soma,média=("%.2f"%soma,"%.2f"%média)


usuários.close
# cria um arquivo para formatar as informações e deixa-las em um tabela
escre= open("arquivos/051relatório.txt","w")
escre.write("ACME Inc.              Uso do espaco em disco pelos usuarios\n")
escre.write("-"*70)
escre.write("\n")
escre.write("Nr.    usuario      Espaco utilizado    % do uso\n")
for i in range(len(lista)):
    escre.write(f"{i+1}      ")
    escre.write(lista[i])
    escre.write("\n")
escre.write("\n")
escre.write(f"Espaco total ocupado = {soma} MB\n")
escre.write(f"Espaco me dio ocupado = {média} MB")