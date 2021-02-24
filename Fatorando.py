n = None

Fat = int(input("Digite um número: ")) 
Fat2 = Fat

for i in range(2,Fat2+1):
    ver = True
    for j in range(2,i):
        if i%j == 0:
            ver = False
            pass
    if ver == True:
        n = i
        while Fat%i == 0:
            Fat/=i
            print(i)
        if Fat == 1:
            exit() 
