n = int(input("Digire um número: "))
soma= 0.0
m=n
for i in range(1, n+1):
     soma += i/m
     m-=1

print(soma)
