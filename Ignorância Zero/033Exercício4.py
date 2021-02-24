def dado(faces):
    import random
    n = random.randint(1,faces)
    return n
faces = int(input("Escolha o número de faces do dado: "))
print("Caiu na face:",dado(faces))