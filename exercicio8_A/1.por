programa
{
	funcao inicio()
	{
		real soma,n
		inteiro i,number

		escreva("Digite a quantidade de valores ")
		leia(number)
		soma = 0.0
		para( i =1;i<=number;i++){
			
			escreva("Digite o "+i+"º numero ")
			leia(n)
			soma = soma + n 
			}
		escreva("A media desses valores é " + (soma/number))
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 219; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */