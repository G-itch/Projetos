txt= "ChicLeTE"
def main():
    print(tudomax(txt))
    print(tudomin(txt))

def tudomax(txt):
    txt2 = ""
    for i in txt:
        if "a" <= i <= "z":
            i = chr(ord(i) + (ord("A") - ord("a")))
        txt2 += i
    return txt2
def tudomin(txt):
    txt3 = ""
    for i in txt:
        if "A" <= i <= "Z" :
            i = chr(ord(i) + (ord("a") - ord("A")))
        txt3 += i
    return txt3

main()