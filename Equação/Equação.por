programa
{
	inclua biblioteca Matematica --> mat 
	real delt,x1,x2,a,b,c
	funcao inicio()
	{
		escreva("Digite o valor de a:")
		leia(a)
		escreva("Digite o valor de b:")
		leia(b)
		escreva("Digite o valor de c:")
		leia(c)

		delt = (b*b) - 4*a*c
		x1 = (-b + mat.raiz(delt,2.0)) / (2*a)
		x2 = (-b - mat.raiz(delt,2.0)) / (2*a)
		escreva("O resultado da equação é:\n")
		escreva("x1 "+x1+"\n")
		escreva("x2 "+x2+"\n")
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 415; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */