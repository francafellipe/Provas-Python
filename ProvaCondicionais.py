#var
velocidadeCarro = int(input('Qual a velocidade do carro ? '))
#inicio
if velocidadeCarro > 80:
    multa = (velocidadeCarro - 80) * 20
    print(f'Você foi multado em {multa} reais.')
else:
    print('Não foi multado !')

#fimalgoritmo