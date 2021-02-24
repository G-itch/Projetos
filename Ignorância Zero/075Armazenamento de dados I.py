import struct
nome = "Ronaldo"
idade = 24
altura = 1.75
x = struct.pack("7s I f",nome.encode(),idade,altura)
print(x)

arq = open("pessoa.cod","wb")
print(arq.write(x))
arq.close()
arq = open("pessoa.cod","rb")
cod_ab = arq.readline()
print(cod_ab)

y = struct.unpack("7s I f",cod_ab)
print(y)

nome2 = y[0].decode()
print(nome2)