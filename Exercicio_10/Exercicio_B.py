x = [];
y = [];
def vizuVeto():
    op = float(input("Digite qual vetor deseja visualizar: \n 1-VetorX \n 2-VetorY"));
    if(op == 1):
        for i in range(N):
            print("O elemento da posição: ",x[i]);
    elif(op == 2):
        for i in range(N):
            print("O elemento da posição: ",y[i]);
def geralM():
    for i in range(N):
        soma = soma + x[i];
        somax = somax + x[i];
        p = p + 1;    
    for i in range(N):
        soma = soma + y[i];
        somay = somay + y[i];
        q = q + 1;
    media = soma/(p+q)
    print("A media dos vetores:",media);
    print("A media do vetor X:",somay/p);
    print("A media do vetor Y:",somax/q);
def maiorGeral():
    for i in range(N):
        if(maior < x[i]):
            maior = x[i];
    for i in range(N):
        if(maior < y[i]):
            maior = y[i];
    print("O maior valor entre os vetores: ", maior);
def troca():
    for i in range(N):
        if(N % 2 == 1):
            xo = float(input("Vetor X\nDigite um novo valor da posição"));
            x.append(xo);
            yo = float(input("Vetor Y\nDigite um novo valor da posição"));
            y.append(yo);
    vizuVeto();
N = int(input("Digite a quantidade para armazenar"));
for i in range(N):
        xo = float(input("Vetor X: Digite o valor da  posição"));
        x.append(xo);
        yo = float(input("Vetor Y: Digite o valor da posição"));
        y.append(yo); 
        somay = somay + y[i];
print("A soma do vetor Y: " , somay);
geralM()
maiorGeral()
vizuVeto()
troca()

