from functools import reduce

def quadrado (numero): # funçao para numeros ao quadrado 
    
    return numero ** 2

def pares (numero): # função para numeros pares

    return numero % 2 == 0 


def soma (x, y ): # funçao soma dos numeros 
    return x + y

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

escolha = (int(input('1 - Visualizar numeros ao quadrado : \n'
                     '2 - Visualizar numeros pares da lista :\n'
                     '3 - Visualizar soma dos numeros :\n')))

if escolha == 1:

    quadrados = list(map(quadrado, numeros))

    print(f'O valor ao quadrado dos numeros é = {quadrados} ')

elif escolha == 2 :

    par = list(filter(pares, numeros))

    print(f'Os numeros pares são : {par}')

elif escolha == 3 :

    somatorio = reduce(soma,numeros)
    
    print (f'A soma dos numeros é = {somatorio} ')

else :
    print('Comando invalido ')
    None
    





