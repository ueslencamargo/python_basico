# Criar uma FUNÇÃO  que múltiplica 2 números inteiros:

# A função tem 2 parâmetros que são a,b números inteiros.

# E o retorno dela vai ser outro inteiro, no caso o resultado da multiplicação.

def mult_two(a:int,b:int)->int:
    return a*b

assert mult_two(3, 2) == 6  # Aqui a função é testada com assert.

#Ou seja, eu chamo ela já enviando os 2 números a serem múltiplicados.

#Caso o resultado não seja correto, vai retorar um erro:
#AssertionError

#Sendo o resultado correto, nada vai aparecer na tela.
