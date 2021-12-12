from dominio import Usuario, Lance, Leilao, Avaliador


luan = Usuario("luan")
lucas = Usuario("lucas")


lance_do_luan = Lance(luan, 150.0)
lance_do_lucas = Lance(lucas, 250.0)

leilao = Leilao("Celular")

leilao.lances.append(lance_do_luan)
leilao.lances.append(lance_do_lucas)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')


avaliador = Avaliador()
avaliador.avalia(leilao)


print(
    f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')
