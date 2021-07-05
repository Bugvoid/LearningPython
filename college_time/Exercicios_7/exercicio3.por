programa
{
	funcao inicio()
	{
		real valor
		inteiro condicao
		escreva("Informe o valor do produto: ")
		leia(valor)
		escreva("Informe a condição de pagamento\n1 para dinheiro ou cheque\n2 para cartão de crédito\n3 para parcelado em 2x\n4 para parcelado em 3x: ")
		leia(condicao)

		escolha(condicao){
			caso 1:
				escreva("Desconto de 10% valor total de R$ "+(valor-(valor*0.1)))
				pare
			caso 2:
				escreva("Desconto de 5% valor total de R$ "+(valor-(valor*0.05)))
				pare
			caso 3:
				escreva("Parcelado em 2x de R$ "+(valor/2))
				pare
			caso 4:
				escreva("Parcelado em 3x de R$ "+(valor+(valor*0.1))/3)
				pare			
		}

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 43; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = vetor, matriz, funcao;
 */