print(" Digite um número que eu direi todos os números primos entre 1 e ele. ")
n = int(input("Qual o número? "))
div= 0
resp = ("Os números primos são: ")
for i in range(1,n+1):
    primo = True
    for j in range(2,i):
        div+=1
        if i%j == 0:
            primo = False
    if primo:
        print(i)
        resp += (" %i" %(i))
    
        

print(resp)

print("Foram feitas %i divisões para chegar nesse resultado" %(div)) 



