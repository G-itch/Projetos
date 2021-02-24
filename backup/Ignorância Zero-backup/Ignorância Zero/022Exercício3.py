colab = float(input("Digite o salário do colaborador: "))

print("Salário antes do reajuste: %g" %colab)
if colab < 280:
    sal = colab + colab/100*20
    per = "20%"
elif 280 < colab < 700:
    sal = colab + colab/100*15
    per = "15"
elif 700 < colab < 1500:
    sal =  colab + colab/100*10
    per = "10%"
elif 1500 < colab:
    sal = colab + colab/100*5
    per = "5%"

print("Percentual do aumento aplicado: %s" %per)

print("Valor do aumento: %.2f" %(sal - colab))

print("Novo salário: %.2f "%sal)





