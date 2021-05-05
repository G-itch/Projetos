x= "frente 4"
y= ""
list = []
for i in x:
    y += i
    if i == " " or i == len(x):
        list.append(y)
        y=""
print(list)