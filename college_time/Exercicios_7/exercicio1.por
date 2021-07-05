programa
{
	funcao inicio()
	{
		real kmAtual, kmAnterior, litros
		escreva("Informe a quilometragem atual: ")
		leia(kmAtual)
		escreva("Informe a quilometragem anterior: ")
		leia(kmAnterior)		
		se(kmAtual < kmAnterior){
			escreva("A quilometragem atual precisa ser maior que a quilometragem anterior.")
		}senao{
			escreva("Informe os litros consumidos: ")
			leia(litros)	
			escreva("A taxa de consumo e "+(kmAtual-kmAnterior)/litros+" litros por quilometro rodado")	
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 454; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = vetor, matriz, funcao;
 */