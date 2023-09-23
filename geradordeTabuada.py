num = int(input('Bem vindo a Tabuada !\n'
                'Qual número deseja ver a tabuada, de 1 a 10 :'))
print(f'A tabuada de {num} é :')


for i in range(1, 11):

    print(f' {num} x {i} = {num*i}')