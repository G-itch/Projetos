import random
lista_n = []
for i in range(20):
    lista_n.append(random.randrange(1000))
ta = int(input("asdasd: "))
lista_n.append(ta)
for j in lista_n:
    x = ""
    y = ""
    z = ""
    n = j
    if n >= 100:
        x = "centena"
    if n >= 200:
        x+= "s"
    if n% 100 >= 10:
        if n%10 == 0:
            x+=" e "
        else:
            x+=", "
        y = "dezena"
        if n%100 >= 20:
            y += "s"
    if n% 10 > 0:
        y +=" e "
        z = "unidade"
        if n% 10 > 1:
            z +="s"
    if n% 100 < 10 and n%10 >0:
        x+=" e "                

    print(j)
    if j //100 == 0 and j% 100 < 10:
        print(str(j%10)+" "+ z)
    elif j //100 == 0 and j% 10 == 0:
        print(str((j//10)-(j//100*10))+" "+y)
    elif j% 100 < 10 and j%10 == 0:
        print(str(j//100)+" "+x)
    elif j//100 == 0 and j%10 != 0:
        print(str((j//10)-(j//100*10))+" "+y+str(j%10)+" "+ z)
    elif j% 100 < 10 and j//100 != 0:
        print(str(j//100)+" "+x +str(j%10)+" "+ z)
    elif j%10 == 0 and j% 100 > 10:
        print(str(j//100)+" "+x +str((j//10)-(j//100*10))+" "+y)        
    elif j//100 != 0 and j%100>=10 and j%10 != 0:   
        print(str(j//100)+" "+x +str((j//10)-(j//100*10))+" "+y+str(j%10)+" "+ z)        
        
