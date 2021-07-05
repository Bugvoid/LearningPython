programa
{
	funcao inicio()
	{
		real altura
		cadeia sexo
		escreva("Informe a sua altura: ")
		leia(altura)
		escreva("Informe o sexo (M ou F): ")
		leia(sexo)

		se(sexo == "M" ou sexo == "H" ou sexo == "homem" ou sexo == "m" ou sexo == "h"){
			escreva("Seu peso ideal e "+((72.7*altura)-58))
		}senao se(sexo == "F" ou sexo == "f" ou sexo == "mulher"){
			escreva("Seu peso ideal e "+((62.1*altura)-44.7))
		}senao{
			escreva("Seu sexo e indefinido muito duvidoso")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 475; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = vetor, matriz, funcao;
 */