programa
{
	funcao inicio()
	{
		real soma,n,maior
		inteiro i,resp

		
		soma = 0.0
		i=0
		faca{
			escreva("Digite um numero ")
			leia(n)
			 maior = 0
			se(n>maior){
				maior = n
				}
			soma = soma + n
			
			i++ 
			escreva("Deseja encerrar?\n 1-Sim 2-N�o ")
			leia(resp)	
			}enquanto(resp == 2)	
			 
			escreva("A media desses valores � " + (soma/i) + "\nO Maior numero desses valores � " + maior)
		

		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta se��o do arquivo guarda informa��es do Portugol Studio.
 * Voc� pode apag�-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 353; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */