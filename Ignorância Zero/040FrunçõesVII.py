x = 2345
def f1():
    def f2():
        global x
        print(x)
        x+=1
    f2()
for i in range(10):
    f1()
