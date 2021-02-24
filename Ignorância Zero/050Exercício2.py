txt = input("Digite algo: ")
txt2 = input("Digite novamente:")
def count(string,sub):
    cont = 0
    for i in range(len(string)+1 - len(sub)):
        if string[i:i+len(sub)] == sub:
            cont += 1
    
    return cont

print(count(txt,txt2))