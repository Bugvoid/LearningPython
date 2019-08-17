def getVelo(d,t):
    res = d/t
    return(res)

d = float(input("Digite a distancia de d "))
t = float(input("Digite o tempo de t "))
d2 = float(input("Digite a distancia de d2 "))
t2 = float(input("Digite o tempo de t2 "))
d3 = float(input("Digite a distancia de d3 "))
t3 = float(input("Digite o tempo de t3 "))

print("A velocidade de d com t é " ,getVelo(d,t))
print("\n A velocidade de d2 com t2 é " ,getVelo(d2,t2))
print("\n A velocidade de d3 com t3 é " ,getVelo(d3,t3))
