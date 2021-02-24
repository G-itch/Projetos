m = int(input("Digite o primeiro número:"))
n = int(input("Digite o segundo número:"))
total = totalMAX = 0
for i in range(m):
    for j in range(n):
        total = (i*j) - (i**2) + j  
        if (total > totalMAX):
            totalMAX = total
            segMax = i
            segNax = j

print("1 =",segNax,"2 =",segMax,"O maior total =",totalMAX)
            