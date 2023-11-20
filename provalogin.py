from tkinter import *


def login():
    senha = senhaentry.get()
    email = emailentry.get()

    if len(senha) >= 6 and '@' in email:
        respotalabel.config(text='Login realizado !!',fg='green', font=('Helvetica', 12, 'bold'))
        senhaentry.delete(0,END)
        emailentry.delete(0,END)
        

    else:
        respotalabel.config(text='Login invalido ',fg='red', font=('Helvetica', 12, 'bold'))
        senhaentry.delete(0,END)
        emailentry.delete(0,END)

    

janela = Tk()
janela.title ('Pagina de login')
janela.resizable(False,False)
janela.geometry('300x200')
janela.configure(bg='#add8e6')

#labels e entrys

emaillabel = Label(janela, text= 'E-mail : ', bg='#add8e6', font=('Helvetica', 10))
emaillabel.pack()
emailentry = Entry(janela, bg='lightgray', font=('Helvetica', 10))
emailentry.pack()
senhalabel = Label(janela, text= 'Senha :', bg='#add8e6', font=('Helvetica', 10))
senhalabel.pack()
senhaentry = Entry(janela, show= '*', bg='lightgray', font=('Helvetica', 10))
senhaentry.pack()

#botao de login

loginbotao = Button(janela, text= 'Entrar',command=login, bg='green', fg='black', font=('Helvetica', 10, 'bold'))
loginbotao.pack()

#label de resposta 

respotalabel = Label(janela,text= '', bg='#add8e6', font=('Helvetica', 12, 'italic'))
respotalabel.pack()



janela.mainloop()