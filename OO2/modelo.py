from abc import ABC  # abstract class
from collections.abc import MutableSequence
from numbers import Complex


class Playlist(MutableSequence):
    pass


class Numero(Complex):
    def __getitem__(self,item):
      super().__getitem__(item)


filmes = Playlist()
filmes = Numero()


class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, new_name):
        self._nome = new_name

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f"Nome: {self._nome} -  {self.ano} - Like: {self._likes}"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self._nome} -  {self.ano} - {self.duracao} min - Like: {self._likes}"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self._nome} -  {self.ano} - {self.temporadas} temp - Like: {self._likes}"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

    # def tamanho(self):
    #     return len(self.programas)


vingadores = Filme("vingadores - ultimato", 2019, 240)
finalSpace = Serie("Final Space", 2020, 3)
endgame = Filme("Endgame", 2018, 200)
onepiece = Serie("One Piece", 1997, 30)

vingadores.dar_like()
vingadores.dar_like()
endgame.dar_like()
endgame.dar_like()
endgame.dar_like()
onepiece.dar_like()
onepiece.dar_like()
onepiece.dar_like()
onepiece.dar_like()
onepiece.dar_like()
finalSpace.dar_like()

# print(f"Nome: {vingadores.nome} - Like: {vingadores.likes}")

# print(f"Nome: {finalSpace.nome} - Like: {finalSpace.likes}")


filmes_e_series = [vingadores, finalSpace, endgame, onepiece]
fim_de_semana = Playlist("Fim de Semana", filmes_e_series)

print(f"Tamanho do playlist: {len(fim_de_semana)}")


for programa in fim_de_semana:
    # if hasattr(programa, "duracao"):
    #     detalhes = programa.duracao
    # else:
    #     programa.temporadas
    # print(f"{programa.nome} - {detalhes} D - {programa.likes}")
    # programa.imprime()
    print(programa)

# print(f"Ta ou não Tá? {endgame in fim_de_semana}")
