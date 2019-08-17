programa
{
	funcao inicio()
	{
		real valor
		inteiro tipo
		escreva("Informe o valor do investimento: ")
		leia(valor)
		escreva("Informe o tipo de investimento: ")
		leia(tipo)

		escolha(tipo){
			caso 1:
				escreva("Investimento escolhido Poupança\n"+
				"Rendimento mensal de 3%\n"+
				"valor corrigido R$ "+(valor+(valor*0.03)))
				pare
			caso 2:
				escreva("Investimento escolhido Fundos de renda fixa\n"+
				"Rendimento mensal de 4%\n"+
				"valor corrigido R$ "+(valor+(valor*0.04)))
				pare
			caso contrario:
				escreva("Informe o tipo de investimento correto")
				pare
				
		}

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 53; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = vetor, matriz, funcao;
 */