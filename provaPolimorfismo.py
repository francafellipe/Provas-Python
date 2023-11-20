class BombaCombustivel :
    def __init__(self,tipocombustivel,valorLitro,quantidadeCombustivel):
        self.tipocombustivel = tipocombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abatecerPorValor (self):
        valorAbastecido = float(input('Qual valor será abastecido ?'))
        quantidadelitros = valorAbastecido / self.valorLitro
        print(f'Valor R$ :{valorAbastecido}\n'
              f'Litros : {quantidadelitros}')
        
        self.quantidadeCombustivel -= quantidadelitros
        
    def abastecerPorLitro(self):
        litroAbatecido = float(input('Quantidade de litros a abastecer ?'))
        valorapagar = litroAbatecido * self.valorLitro
        print (f'Valor a ser pago R$:{valorapagar} ')
        self.quantidadeCombustivel -= litroAbatecido

    def alterarValor(self):
        novoPreco = float(input('Preço atualizado = '))
        self.valorLitro = novoPreco
        print(f'O valor do litro agora é R$:{self.valorLitro}')

    def alterarCombustivel(self):
        novoCombustivel = input('Qual combustivel vai abastecer a bomba agora ')
        self.tipocombustivel = novoCombustivel
        print(f'Combustivel atualizado agora temos : {novoCombustivel}')

    def alterarQuantidadedeCombustivel(self):
        novaQuantidade = float(input('QUal a nova quantidade de combustivel disponivel :'))
        self.quantidadeCombustivel = novaQuantidade
        print(f'Quantidade de combustivel atualizada : {self.quantidadeCombustivel} litros ')

bomba = BombaCombustivel("Etanois", 7.50, 1000)
while True:
    escolha = int(input('Como deseja abastecer ? \n'
                        '1- Por valor ? \n'
                        '2- Por litros \n'
                        '3- Atualizar preço do combustivel \n'
                        '4- Alterar combustivel na bomba \n'
                        '5- Abastecer a bomba de combustivel.\n'
                        '0 - Finalizar '))
    if escolha == 1 :
        bomba.abatecerPorValor()
    elif escolha == 2 :    
        bomba.abastecerPorLitro()
    elif escolha == 3:
        bomba.alterarValor()
    elif escolha == 4:
        bomba.alterarCombustivel()
    elif escolha == 5:
        bomba.alterarQuantidadedeCombustivel()
    elif escolha == 0 :
        break
    else:
        print('Escolha um numero entre as opçoes ')
