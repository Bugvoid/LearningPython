
import math

a=float(input("Insira o valor de a \n"))
b=float(input("Insira o valor de b \n"))
c=float(input("Insira o valor de c \n"))
delt = (b*b) - 4*a*c
delt =math.sqrt(delt)
x1= (-b+delt)/(2*a)
x2= (-b-delt)/(2*a)
print ("o resultado da equação é:\n")
print ("x1:",x1,"\n")
print ("x2:",x2)
