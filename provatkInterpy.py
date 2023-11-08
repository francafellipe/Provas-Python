from tkinter import *
from tkinter import Tk
def calcular():
    valoremCm = float(entradacm.get())
    resultado.config(text=f'Valor em Metros e : {valoremCm / 100} m') 

janela = Tk()

janela.title('Conversor')

frame1 = Frame(janela)
frame1.pack()

pediramedida = Label(frame1, text='Digite o valor em cm ?')
pediramedida.pack()

entradacm = Entry(frame1)
entradacm.pack()

botaocalc = Button(frame1 , text='Calcular', bg= 'green', command= calcular)
botaocalc.pack()

mostrar = Label(frame1,text= 'Valor em Metros é ')
mostrar.pack()

resultado = Label(frame1, text='')
resultado.pack()


janela.mainloop()