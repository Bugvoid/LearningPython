import math
def getDelta(a,b,c):
    res = (b*b) -4*a*c
    return(res)

def getX1(a,b,c,getDelta):
        res = (-b + math.sqrt(getDelta))/(2*a)
        return(res)

def getX2(a,b,c,getDelta):
        res = (-b - math.sqrt(getDelta))/(2*a)
        return(res)


a= float(input("Digite o valor de a"))
b= float(input("Digite o valor de b"))
c= float(input("Digite o valor de c"))
print ("O valor de delta é ",getDelta(a,b,c),"O valor de x1 é ",getX1(a,b,c,getDelta(a,b,c)),
       "O valor de x2 é ",getX2(a,b,c,getDelta(a,b,c)))


