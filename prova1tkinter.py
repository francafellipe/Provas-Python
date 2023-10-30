from tkinter import *
from tkinter import messagebox
def exibir_mensagem():
    nome_inserido = nome.get()
    mensagem = f'Olá , {nome_inserido}! Bem vindo ao sistema de cadastrar '
    messagebox.showinfo('Mensagem de boas vindas !', mensagem)
janela = Tk()


janela.title('Sistema de Cadastro ')
janela.geometry('300x250')

inserirnome = Label (janela,text = 'Digite seu nome ')
inserirnome.pack()

nome = Entry(janela)
nome.pack()

enviarnome = Button(janela,text= 'Enviar' , command=exibir_mensagem)
enviarnome.pack()



janela.mainloop()