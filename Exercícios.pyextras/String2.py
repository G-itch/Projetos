txt = input("Digite alguma coisa: ")
txt = txt.upper()
for i in range(len(txt)-1,-1,-1):
    print(txt[i], end ="")

