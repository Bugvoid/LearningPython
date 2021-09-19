url = "https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"


# print(url)
# url_query = url[20:38]
# print(url_query)

# url_base = url[0:20]
# print(url_base)


# indices = url.find("?")
# url_params = url[:indices]
# url_params2 = url[indices+1:]

# print(url_params)
# print(url_params2)

# Separa base e os parametros
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de parametro
parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)

url = "https://www.alura.com.br/curso?curso=python"
indice_curso = url.find("curso")
indice_valor = indice_curso + len("curso") + 1
valor = url[indice_valor:]
print(valor)
