from collections import Counter
from collections import defaultdict
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_leraning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_leraning)

print(assistiram)

print(set(assistiram))
set([1, 2, 3, 1])


for usuario in set(assistiram):
    print(usuario)


usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_leraning = {13, 23, 56, 42}  # Não tem index, mas pode for

print(usuarios_data_science | usuarios_machine_leraning)

print(usuarios_data_science & usuarios_machine_leraning)


fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_leraning
print(15 in fez_ds_mas_nao_fez_ml)

print(23 in fez_ds_mas_nao_fez_ml)

print(usuarios_data_science ^ usuarios_machine_leraning)


usuarios = {1, 2, 3, 47, 57, 67, 77, 80}

usuarios.add(47)

usuarios.add(57)


usuarios = frozenset(usuarios)

type(usuarios)

meu_texto = "Good thinkings"
set(meu_texto.split(' '))


aparicoes = {
    "Luan": 1,
    "dale": 2,
    "nome": 2,
    "vindo": 1,
}

type(aparicoes)  # dict


print(aparicoes["Luan"])

print(aparicoes.get('xpto', 0))


aparicoes = dict(Luan=2, dale=3)


aparicoes = {
    "Luan": 1,
    "dale": 2,
    "nome": 2,
    "vindo": 1,
}
aparicoes["teste"] = 2

del aparicoes["teste"]

"Carlos" in aparicoes


for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)


for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(elemento)


meu_texto = "Bem vindo meu nome é Luan eu gosto muito de nomme e tenho o meu cachorro"

meu_texto = meu_texto.lower()

aparicoes = {}

for palavras in meu_texto.split():
    ate_agora = aparicoes.get(palavras, 0)
    aparicoes[palavras] = ate_agora + 1

print(aparicoes)


aparicoes = defaultdict(int)

for palavras in meu_texto.split():
    aparicoes[palavras] += 1

print(aparicoes)


class Conta:
    def __init__(self):
        print("Imprimindo conta")


conta = defaultdict(Conta)

conta[15]


aparicoes = Counter(meu_texto.split())

print(aparicoes)
