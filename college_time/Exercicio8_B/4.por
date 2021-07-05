programa
{
	funcao inicio()
	{
		inteiro n = 0,y=0,x=0
		real mediam=0.0,mediah =0.0,altura = 0.0
		caracter sexo 
		escreva("Digite a quantidade de pessoas no grupo")
		leia(n)
		para(inteiro i=0;i<n;i++){
			escreva("Digite a estatura da pessoa")
			leia(altura)
			escreva("Digite o sexo da pessoa")
			leia(sexo)

			se(sexo == 'F' ou sexo == 'f'){
				mediam += altura
				x++
				}senao{
				mediah+= altura
				y++
					}
			}
		escreva("A estatura das mulheres: " + (mediam/x) +
				"\nA estatura dos homens: " + (mediah/y))
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 494; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */