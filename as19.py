a=int(input("a :"))
b=int(input("b :"))
c=int(input("c :"))
d=int(input("d :"))
z1=(a,b)
z2=(c,d)
def addComplex( z1, z2): 
    return z1 + z2 
z1 = complex(a,b) 
z2 = complex(c,d) 
print( "Addtion is : ", addComplex(z1, z2)) 
def subComplex( z1, z2): 
    return z1 - z2 
z1 = complex(a,b) 
z2 = complex(c,d) 
print( "Substraction is : ", subComplex(z1, z2))
def mulComplex( z1, z2): 
    return z1 * z2 
z1 = complex(a,b) 
z2 = complex(c,d) 
print( "Multiplication is : ", mulComplex(z1, z2))
def divComplex( z1, z2): 
    return z1 / z2 
z1 = complex(a,b) 
z2 = complex(c,d) 
print( "Division is : ", divComplex(z1, z2))