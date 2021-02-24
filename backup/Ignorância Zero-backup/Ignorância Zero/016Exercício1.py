print("Verifique se um número é palíndromo")

n = int(input("Digite o número maior que 10: "))

aux=n
dig=reverso=0
while aux > 0 :
    dig = aux % 10
    reverso = reverso * 10 + dig
    aux //= 10

if reverso == n:
    print("O número",n,"é palíndromo")
else:
    print("O número",n,"não é palíndromo")