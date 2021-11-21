from Cpf_Cnpj import Documento
from validate_docbr import CNPJ
import re
from telefones import Telefones
from datetime import datetime, timedelta
from datas_br import DatasBr
from acesso_cep import BuscaEndereco
# cpf = 15896347884
# objeto_cpf = Cpf(cpf)

# print(objeto_cpf)

# cpf_um = Cpf("15316264754")


# print(cpf_um)

# teste = "35379838000112"
# teste2 = "32007832062"
# cnpj = CNPJ()


# print(cnpj.validate(teste))

# documento = Documento.cria_documento(teste)
# documento2 = Documento.cria_documento(teste2)
# print(documento)
# print(documento2)

# padrao = "[0-9][a-z]{2}[0-9]"
# texto = "123 1a2 1cc aa1"
# resposta = re.search(padrao, texto)
# print(resposta.group())

# padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
# texto = "aaabbbccc luan123@gmail.com.br"
# resposta = re.search(padrao, texto)
# print(resposta.group())

# padrao_molde = "(xx)aaaa-wwww"
# padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"

# telefone = "552126481234"
# telefone_Objeto = Telefones(telefone)

# print(telefone_Objeto)

# cadastro = DatasBr()
# print(cadastro.tempo_castro())
cep = "08421570"
obejto_cep = BuscaEndereco(cep)
bairro, cidade, uf = obejto_cep.acessa_via_cep()
print(bairro, cidade, uf)
