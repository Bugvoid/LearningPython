programa
{
	funcao inicio()
	{
		real soma,n,menor,pos,neg
		inteiro i,resp

		pos=0.0
		neg=0.0
		soma = 0.0
		i=0
		 menor = 0.0
		faca{
			escreva("Digite um numero ")
			leia(n)
			
			 se(n<0){
			 	neg++
			 	}senao{
			 		pos++
			 		}
			 
			se(n<menor){
				menor = n
				}
			soma = soma + n
			
			i++
			escreva("Deseja encerrar?\n 1-Sim 2-Não ")
			leia(resp)	
			}enquanto(resp == 2)	
			 
			escreva("A media desses valores é " + (soma/i) 
			+ "\nO Menor numero desses valores é " + menor
			+ "\nOs numeros positivos são: " + pos
			+ "\nOs numeros negativos são:" + neg)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 130; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */