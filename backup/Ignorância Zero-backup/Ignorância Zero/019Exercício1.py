x,y,z= input("Digite os três lados de um triângulo:").split()
x,y,z= [int(x),int(y),int(z)]
if (x**2 + y**2 == z**2) or (x**2 + z**2 == y**2) or (z**2 + y**2 == x**2):
    print("O triângulo é retângulo")