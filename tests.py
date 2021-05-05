string = "Hello"
print("".join([i.upper() if val % 2 == 0 else i.lower() for val,i in enumerate(list(string))]))