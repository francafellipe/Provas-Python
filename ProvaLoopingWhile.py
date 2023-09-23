
contador = 0 
somatorio = 0

while True :
    escolha = int(input('Escolha uma opçao :  : \n'
                        'Digite 0 para parar  \n'
                        'Digite 1 para somar  \n'))
    if escolha == 1:
        numeros = int(input('Digite um numero : '))
        somatorio += numeros
        contador +=1
        media = somatorio/contador
    if escolha == 0:
        print(f'A soma dos {contador} numeros digitados foi {somatorio}, a media dos números é {media}')
        break
    
    


 
