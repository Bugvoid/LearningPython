programa
{	inclua biblioteca Matematica --> mat
	funcao inicio()
	{
		real x,y,z

		escreva("Digite o valor de x ")
		leia(x)
		escreva("Digite o valor de y ")
		leia(y)
		escreva("Digite o valor de z ")
		leia(z)

		escreva("O valor do delta � " + getDelta(x,y,z))
		escreva("O valor do X1 � " + getX1(x,y,z))
		escreva("O valor do X2 � " + getX2(x,y,z))
		
	}
	funcao real getDelta(real a,real b,real c) {
				real res
				res =  (b*b) - 4*a*c
				retorne(res)
			}
	funcao real  getX1(real a,real b,real c){
			real res
			res = (-b + mat.raiz(getDelta(a,b,c),2.0))/(2*a)
			retorne(res)
		}
		funcao real  getX2(real a,real b,real c){
			real res
			res = (-b - mat.raiz(getDelta(a,b,c),2.0))/(2*a)
			retorne(res)
		}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta se��o do arquivo guarda informa��es do Portugol Studio.
 * Voc� pode apag�-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 445; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */