"""arquivo = open("OláArquivo.txt","w")
arquivo.write("Hello World")
arquivo.write("\n")
arquivo.write("Ola Mundo")
arquivo.writelines(["Ola","Mundo","essa","eh","nossa","primeira","aula"], end="")
arquivo.close()"""
"""
arquivo = open("OláArquivo.txt","r")
arquivo.readline()
x = arquivo.readlines()

print(x)
arquivo.close()"""

arquivo = open("OláArquivo.txt","a")
arquivo.write("\nnovalinha")
arquivo.close()