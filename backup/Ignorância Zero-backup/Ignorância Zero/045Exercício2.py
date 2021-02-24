n = int(input("Digite um número: "))
fat = n
print(f"Fatorial de {n}") 
print(f"{n}! =",n, end="")
while n-1 >= 1:
    n -= 1
    fat *= n
    print(f" . {n}", end="")
print(" =",fat)
    

