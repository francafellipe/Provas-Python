class Material :
    def __init__(self, titulo,autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora


    def exibir_informacoes (self):
        print (f'Titulo :{self.titulo} \n E criado por :{self.autor_ou_editora}' )
    
class Livro (Material):
    def __init__(self, titulo, autor_ou_editora,genero):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Gênero : {self.genero}')
    
class Revista (Material):
    def __init__(self, titulo, autor_ou_editora,edicao):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Ediçao : {self.edicao}')
    

harrypotter = Livro('Harry Potter ','GK Rowlling','Fantasia ')
oeste = Revista('Revista Oeste','Olavo de carvalho','6 Edição')
harrypotter.exibir_informacoes()
oeste.exibir_informacoes()

    