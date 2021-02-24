nt = int(input("Defina o número de temperaturas: "))

tempT = 0  
f = 1
for i in range (1,nt+1):
    temp = float(input("Defina a %i temperatura: " %i))
    while f == 1:
        tempMax = temp
        tempMin = temp
        f +=1
        
    if temp > tempMax :
        tempMax = temp
    if temp < tempMin :
        tempMin = temp
    tempT += temp
tempM = tempT/nt

print("A maior temperatura foi de %s°C"%tempMax)
print("A menor temperatura foi de %s°C"%tempMin)
print("A temperatura média foi de %.2f°C"%tempM)




