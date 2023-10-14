#Class
#Syntaxe
#construtor ou propriedades 
class Elevador :
    def __init__(self,totalCapacidade,totalAndar): # nao se sabe qual o andar nem quantas pessoas ainda no elevador 
        self.totalCapacidade =  totalCapacidade
        self.atualCapacidade = 0
        self.totalAndar = totalAndar
        self.atualAndar = 0

    def Subir(self):# mostrar qual andar estar , e mostre subindo , se estiver no maximo mostrar que estar no mais alto 
        if self.atualAndar < self.totalAndar :
            self.atualAndar+= 1 
            print(f'Subindo ')

        else:
            print('VOCÊ ESTÁ NO ANDAR MAIS ALTO!')
    def Descer(self):
        if self.atualAndar > 0 :
            self.atualAndar -= 1

            print(f'Descendo')

        else: 
            print('VOCÊ JÁ ESTÁ NO TÉRREO !')

    def Entrar(self):
        if self.atualCapacidade < self.totalCapacidade :
            self.atualCapacidade += 1 
            print('Entrando uma pessoa')

        else:
            print ('O ELEVADOR ESTÁ CHEIO !')

    def Sair (self):
        if self.atualCapacidade >= 1 :
            self.atualCapacidade -= 1 
            print('Saindo uma pessoa !')

        else : 
            print ('NÃO TEM NINGUÉM')


elevador1 = Elevador(10,50 )#defininir capacidade maxima , total de andares 

elevador1.Subir()
elevador1.Descer()
elevador1.Entrar()
elevador1.Sair()

#metodos ou funcoes 