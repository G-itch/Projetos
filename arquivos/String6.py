txt = input("Digite algo: ")
def s(x=0):
    global txt
    if len(txt)-x == 0:
        exit()
    else:
        for i in range(0,len(txt)-x):
            print(txt[i], end="")
        print("")
        return s(x+1)
    
print(s())