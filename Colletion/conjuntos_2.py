from collections import Counter
from collections import defaultdict

texto1 = """
  Quando falamos de frameworks CSS um dos principais nomes que aparecem é Bootstrap. Mas recentemente um novo concorrente apareceu no mercado: o Tailwind. Os dois têm como princípio ajudar no desenvolvimento de páginas, mas ambos funcionam de maneiras bem diferentes. Então qual usar?

Bootstrap
Criado pela Twitter em 2011, o Bootstrap surgiu em um hackaton para padronizar o uso de ferramentas no desenvolvimento interno da empresa, evitando muitas manutenções e melhorando a consistência dos projetos. Bootstrap é um framework baseado em componentes. É pensado principalmente em desenvolvimento mobile-first. Sua prioridade é a responsividade.

Ele possui uma estilização pré definida, que chamamos de UI Kits, e qualquer customização precisa ser feita com a sobrescrita em um arquivo CSS próprio. Uma das grandes vantagens de usar Bootstrap é que componentes como menu laterais, cartões e carrousels já tem suas lógicas montadas, isso quer dizer que basta criar a sua estrutura e adicionar as classes corretas e sua funcionalidade é automaticamente implementada. Sem contar, novamente, tudo responsivo.

Tailwind: o que é?
Outro framework que vem ganhando notoriedade no mercado é o Tailwind. Criado em 2017 é um framework baseado em utilidades e tem como prioridade a facilidade de customização.

Estilizar elementos com Tailwind é quase como escrever estilizações inline (escrever CSS dentro do atributo style), só que com classes. Por isso ele é um framework focado em utilidades. Classes como text-blue-600 para mudar a cor do texto de um elemento são muito utilizadas. A grande vantagem é que não precisamos seguir um padrão visual pré definido pelo framework.

"""

texto2 = """
  Ciência de Dados é um campo que tem ganhado cada vez mais espaço em outras áreas, outros mercados. Durante a Semana Dados, você pôde ver isso de perto ao conhecer as incríveis intersecções de Data Science com o mercado financeiro e a área de esportes.

Mas não é só isso. Uma pesquisa recente da Intera mostrou que a demanda por profissionais na área de dados teve um crescimento de quase 500% no primeiro semestre deste ano. É surpreendente como empresas ao redor do mundo estão se tornando cada vez mais data-driven.

Agora, chegou a hora de você fazer parte deste movimento. Por isso, te pergunto: onde você está usando a Ciência de Dados? Porque o próximo passo da sua carreira pode começar aqui.

Na segunda-feira desta semana, abrimos as matrículas para a terceira edição do Bootcamp Data Science da Alura. Temos novidades, módulos reestruturados e um foco ainda maior no mercado de trabalho, está sensacional!

Este Bootcamp tem sido importante para a transformação profissional de inúmeros alunos e alunas. Quer saber mais? Então conheça a história da Letícia Pires e do Marivaldo Torres, cientistas que se formaram com a gente e estão atuando na área.

No site do programa, você fica por dentro de todo o conteúdo do Bootcamp e de várias outras informações relacionadas a ele.

Se você já é um aluno ou aluna da Alura, aproveite, porque tem um desconto especial de R$250 esperando por você — que, inclusive, é cumulativo com outros descontos vigentes no momento da matrícula.

Ah! E depois do Bootcamp, vai ser muito legal se você me marcar nas suas redes sociais para eu dar uma olhada no seu portfólio, depois de pronto.

Bom, por enquanto é isso. Desejo a você mergulhos cada vez mais profundos no universo de Data Science!
"""


aparicoes = Counter(texto1.lower())
total_de_caracteres = sum(aparicoes.values())
for letra, frequencia in aparicoes.items():
    tupla = (frequencia / total_de_caracteres)
    print(tupla)


[(frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]

proporcoes = [(letra, frequencia / total_de_caracteres)
              for letra, frequencia in aparicoes.items()]
proporcoes = Counter(dict(proporcoes))

proporcoes.most_common(10)


def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto1.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres)
                  for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comums = proporcoes.most_common(10)
    for caractere, proporcao in mais_comums:
        print("{} => {:2f}%".format(caractere, proporcao * 100))


analisa_frequencia_de_letras(texto1)
