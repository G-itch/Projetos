txt = input("Digite uma string: ")
txt2= input("Digite outra string: ")
print("A string \"{}\" tem {} caracteres".format(txt,len(txt)))
print("A string \"{}\" tem {} caracteres".format(txt2,len(txt2)))
if len(txt) == len(txt2):
    print("As duas strings possuem o mesmo tamanho")
else:
    print("As duas strings não possuem o mesmo tamanho")
if txt == txt2:
    print("As duas strings possuem o mesmo conteúdo")
else:
    print("As duas strings não possuem o mesmo conteúdo")
    type(txt)