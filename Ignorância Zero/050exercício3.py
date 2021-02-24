txt = input("Digite algo: ")
txt2 = input("Digite novamente: ")
txt3 = input("Digite para o que vai ser mudado: ")
def replace(string,sub,m):
    palavra = ""
    cont1 = 0
    ver = True
    for i in range(len(string)):
        if string[i:i+len(sub)] == sub:
            palavra += m
            cont1 = i+len(sub)
            ver = False
        else:
            print(cont1)
            if i >= cont1 or ver: 
                palavra += string[i]  
    return palavra

print(replace(txt,txt2,txt3))