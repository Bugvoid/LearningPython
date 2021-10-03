idades = [39, 30, 12, 27]
type(idades)  # list
print(idades[0])
idades.append(80)
print(idades)
idades.remove(80)
print(idades)
idades.insert(0, 80)

for idade in idades:
    print(f"idade {idade}")

idades = [20, 55, 78, 89]
idades.extend([55, 89])
print(idades)

idades_no_ano_vem = []
for idade in idades:
    idades_no_ano_vem.append(idade+1)
print(idades_no_ano_vem)
# list_crompreension
print([(idade+1) for idade in idades])
def proximo_ano(idade):
    return idade+1
print([proximo_ano(idade) for idade in idades if idade > 21])


def faz_processamento_de_visualizacao(lista=None):
    if lista is None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)


idades = [20, 55, 44, 56, 10]
faz_processamento_de_visualizacao(idades)
faz_processamento_de_visualizacao()
