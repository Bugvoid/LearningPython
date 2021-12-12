from unittest import TestCase
from src.dominio import Usuario, Leilao, Lance


class TestLeilao(TestCase):

    def setUp(self):
        self.luan = Usuario("luan",500.0)
        self.lance_do_luan = Lance(self.luan, 150.0)
        self.leilao = Leilao("Celular")

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        lucas = Usuario("lucas", 500.0)
        lance_do_lucas = Lance(lucas, 250.0)

        self.leilao.propoe(self.lance_do_luan)
        self.leilao.propoe(lance_do_lucas)

        # avaliador = Avaliador()
        # avaliador.avalia(self.leilao)

        menor_valor_esperado = 150.0
        maior_valor_esperado = 250.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
    #     lucas = Usuario("lucas")
    #     lance_do_lucas = Lance(lucas, 250.0)
    #     self.leilao.propoe(lance_do_lucas)
    #     self.leilao.propoe(self.lance_do_luan)

    #     # avaliador = Avaliador()
    #     # avaliador.avalia(self.leilao)

    #     menor_valor_esperado = 150.0
    #     maior_valor_esperado = 250.0
    #     self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
    #     self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_descrescente(self):
        with self.assertRaises(ValueError):
            lucas = Usuario("lucas", 500.0)
            lance_do_lucas = Lance(lucas, 250.0)
            self.leilao.propoe(lance_do_lucas)
            self.leilao.propoe(self.lance_do_luan)

            # avaliador = Avaliador()
            # avaliador.avalia(self.leilao)

            # menor_valor_esperado = 150.0
            # maior_valor_esperado = 250.0
            # self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
            # self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_luan)

        # avaliador = Avaliador()
        # avaliador.avalia(self.leilao)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        lucas = Usuario("lucas", 500.0)
        lance_do_lucas = Lance(lucas, 250.0)
        dale = Usuario("Dale", 500.0)
        lance_do_dale = Lance(dale, 500.0)

        self.leilao.propoe(self.lance_do_luan)
        self.leilao.propoe(lance_do_dale)
        self.leilao.propoe(lance_do_lucas)

        # avaliador = Avaliador()
        # avaliador.avalia(self.leilao)

        menor_valor_esperado = 150.0
        maior_valor_esperado = 500.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_dev_permitir_propor_um_lance_caso_o_leolaio_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_luan)

        quantidade_de_lances_recebida = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebida)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        lucas = Usuario("lucas", 500.0)
        lance_do_lucas = Lance(lucas, 250.0)

        self.leilao.propoe(self.lance_do_luan)
        self.leilao.propoe(lance_do_lucas)

        quantidade_de_lances_recebida = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebida)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_luan2 = Lance(self.luan, 200.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_luan)
            self.leilao.propoe(lance_do_luan2)
