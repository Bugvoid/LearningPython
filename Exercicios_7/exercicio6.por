programa
{
	funcao inicio()
	{
		inteiro idade
		cadeia sexo
		escreva("Informe a sua idade: ")
		leia(idade)
		escreva("Informe o sexo (M ou F): ")
		leia(sexo)

		se(sexo == "M" ou sexo == "H" ou sexo == "homem" ou sexo == "m" ou sexo == "h"){
			se(idade <= 12){
				escreva("Pre�o da diaria e R$ 19,50")
			}senao se(idade > 12 e idade <=55){
				escreva("Pre�o da diaria e R$ 60,30")
			}senao{
				escreva("Pre�o da diaria e R$ 45,50")
			}
		}senao se(sexo == "F" ou sexo == "f" ou sexo == "mulher"){
			se(idade <= 12){
				escreva("Pre�o da diaria e R$ 21,50")
			}senao se(idade > 12 e idade <=55){
				escreva("Pre�o da diaria e R$ 53,99")
			}senao{
				escreva("Pre�o da diaria e R$ 40,00")
			}
		}senao{
			escreva("Seu sexo e indefinido muito duvidoso")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta se��o do arquivo guarda informa��es do Portugol Studio.
 * Voc� pode apag�-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 660; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = vetor, matriz, funcao;
 */