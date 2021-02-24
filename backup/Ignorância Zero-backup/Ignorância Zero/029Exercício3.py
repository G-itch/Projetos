nt = []
np = []

n = None
cont = 0
while n != -1:
  cont += 1
  n = int(input("Digite o %i número: " %cont))
  if n%2 == 0: 
    nt.append(n)

print("Os números pares da sequência são : ",str(nt).strip("[]"))


 