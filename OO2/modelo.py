class Programa():
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

class Filme(Programa):
  def __init__(self, nome, ano,duracao):
      super().__init__(nome,ano)
      self.duracao = duracao
  
class Serie(Programa):
  def __init__(self, nome, ano,temporadas):
      super().__init__(nome,ano)
      self.temporadas = temporadas
    

vingadores = Filme("vingadores - ultimato", 2019, 240)
finalSpace = Serie("Final Space", 2020, 3)

vingadores.dar_like()
vingadores.dar_like()
finalSpace.dar_like()

print(f"Nome: {vingadores.nome} - Like: {vingadores.likes}")

print(f"Nome: {finalSpace.nome} - Like: {finalSpace.likes}")




