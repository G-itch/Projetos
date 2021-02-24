arquivo = open("arquivos/052teste.txt","w")
arquivo.write("Ola\n")
arquivo.write("meu\n")
arquivo.write("nome\n")
arquivo.write("eh\n")
arquivo.write("Enzo")
arquivo.close()
arquivo = open("arquivos/052teste.txt","rb")
print(arquivo.readlines())
arquivo.close()
arquivo = open("arquivos/052teste.txt","r")
arquivo.seek(10)
print(arquivo.readline())
print(arquivo.tell())
arquivo.close
arquivo = open("arquivos/052teste.txt","r")
"""for x in arquivo:
    print(x)"""
for y in arquivo.readline():
    print(y)
