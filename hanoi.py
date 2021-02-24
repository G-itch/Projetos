def move(f,t):
    print("Move {} to {}".format(f,t))
def hanoi(n,f,h,t):
    if n == 0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

hanoi(5,"A","B","C")