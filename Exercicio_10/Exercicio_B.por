programa
{	real x[], y[]
	inteiro N , i 
	funcao inicio()
	{
		
		real somay =0.0 , somax = 0.0
		
		escreva("Digite a quantidade para armazenar")
		leia(N)

		para(i = 0;i < N; i++){
			escreva("Vetor X: Digite o valor da " + i + "º posição")
			leia(x[i])

			escreva("Vetor Y: Digite o valor da " + i + "º posição")
			leia(y[i])
			somay += y[i]
		}
		

		escreva("A Soma do vetor Y: " + somay)
		geralM()
		maiorGeral()
		vizuVeto()
		troca()

	}
	funcao vazio vizuVeto(){
		inteiro op = 0
		escreva("Digite qual vetor deseja visualizar: \n1-VetorX \n 2-VetorY")
		leia(op)
			se(op == 1){
				para(i = 0; i< N; i++){
				escreva("O elemento da posição " + i + "º :" + x[i])
				
			}
		}senao se(op == 2){
			para(i = 0; i< N; i++){
				escreva("O elemento da posição " + i + "º :" + y[i])
				
			}
		}
		
	}
	funcao vazio geralM(){
		real media = 0.0
		real soma = 0.0
		real somax = 0.0
		real somay = 0.0
		real p=0.0,q=0.0
		para (i=0; i<N;i++){
			soma += x[i]
			somax += x[i]
			p++
			}
		para (i=0; i<N;i++){
			soma += y[i]
			somay += y[i]
			q++
			}
			media = soma/(p+q)
			
		escreva("A media dos vetores: " + media)
		escreva("A media do vetor Y: " + somay/q)
		escreva("A media do vetor X: " + somax/p)
		}
	funcao vazio maiorGeral(){
		
		real maior = 0.0
		real p=0,q=0
		para (i=0; i<N;i++){
			se(maior < x[i]){
				maior = x[i]
				}
			}
		para (i=0; i<N;i++){
			se(maior < y[i]){
				maior = y[i]
				}
			}
			
		escreva("O maior valor entre os vetores: " + maior)
		}
		funcao vazio troca(){
		
		real maior = 0.0
		
		para (i=0; i<N;i++){
			se(N % 2 == 1){
				escreva("Vetor X\n Digite um novo valor da posição" + i+" º:")
				leia(x[i])
				escreva("Vetor Y\n Digite um novo valor da posição" + i+" º:")
				leia(y[i])
				}
			}
		vizuVeto()	
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 578; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */