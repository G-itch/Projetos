def tabuada(x,y=1):
        def num(z=1):
            nonlocal x
            if x+1 == z:
                return x
            print(y,"X",z, "=",y*z)
            return num(z+1)
        num()
        if x == y:
            return x
        return tabuada(x,y+1)
        

tabuada(10)
