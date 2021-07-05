programa
{
	funcao inicio()
	{
		real d,t,d2,t2,d3,t3

		escreva("Digite a distancia de d ")
		leia(d)
		escreva("Digite o tempo de t ")
		leia(t)
		escreva("Digite a distancia de d2 ")
		leia(d2)
		escreva("Digite o tempo de t2 ")
		leia(t2)
		escreva("Digite a distancia de d3 ")
		leia(d3)
		escreva("Digite o tempo de t3 ")
		leia(t3)

		escreva("\n A velocidade de d com t é "+ getVelo(d,t))
		escreva("\n A velocidade de d2 com t2 é "+ getVelo(d2,t2))
		escreva("\n A velocidade de d3 com t3 é "+ getVelo(d3,t3))		
	}
	funcao real getVelo(real d,real t){
			real res
			res= d/t
			retorne(res)
			}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 472; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */