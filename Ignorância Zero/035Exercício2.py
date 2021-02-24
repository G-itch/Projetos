def soma(*num):
    return sum(num)

def média(p1,p2,p3,pe1=1,pe2=1,pe3=1):
    return ((p1*pe1) + (p2*pe2) + (p3*pe3))/(soma(pe1,pe2,pe3))

print(média(6,5,5,2,))
print(soma(1,1,1))