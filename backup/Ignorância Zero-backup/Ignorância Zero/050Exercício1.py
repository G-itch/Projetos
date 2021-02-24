
txt = input("Digite algo:")
txt2 = input("Digite novamente: ")
def find():
    global txt,txt2
    for i in range(len(txt)+1 - len(txt2)):
        meh = False
        if txt[i:i+len(txt2)] == txt2:
            print("OK BOOMER")
            break
        else:
            meh = True
    if meh:
        print("Meh")
def index():
    global txt,txt2
    lista = []
    for i in range(len(txt)+1 -len(txt2)):
        if txt[i:i+len(txt2)] == txt2:
            lista.append(i)
    print(lista)
find()
index()