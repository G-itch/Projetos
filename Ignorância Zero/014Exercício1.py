emp = int(input("Digite o número de empresas: "))
meses = int(input("Digite o número de meses: "))

cont = 1
while cont <= emp:
    print("Empresa",cont,": ")
    cont1 = 1
    totalmes = 0
    while cont1 <= meses:
        print("Mês",cont1) 
        ganho = int(input("Digite o ganho da empresa no mês: "))
        gasto = int(input("Digite o gasto da empresa no mês: "))
        totalmes = totalmes + (ganho - gasto)
        cont1 = cont1 + 1
        
    if totalmes < 0 :
        print("A empresa",cont,"teve défict ( balança = R$",totalmes,")")
        if totalmes > 0 :
            print("A empresa",cont,"teve lucro ( balança = R$",totalmes,")")
    else:
        print("A empresa",cont,"ficou indiferente ( balança = R$",totalmes,")")
    
    cont = cont + 1

   
    
    
    


