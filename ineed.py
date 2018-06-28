import json
import requests
from Tkinter import *
from PIL import Image, ImageTk

# response = requests.get("http://jsonplaceholder.typicode.com/comments")

def comando(op):
    if (op == 1):
        print('Quero ir ao banheiro!')
        # print response.status_code
        response = requests.post("http://localhost/bathroom",data=None)
        print(response)

    elif (op == 2):
        print('Estou com fome!')
        # print response.status_code
        response = requests.post("http://localhost/food",data=None)
        print(response)        
        
    elif (op == 3):
        print('Socorro!')
        # print response.status_code
        response = requests.post("http://localhost/help",data=None)        
        print(response)

    elif (op == 4):
        print('Estou com sono!')
        # print response.status_code
        response = requests.post("http://localhost/sleep",data=None)        
        print(response)

janela = Tk()

janela.title('iNeed')

janela.geometry('700x250')

#Banheiro

texto1 = Label(text='Banheiro', fg='blue')
texto1.place(x=50,y=70)

ico1 = ImageTk.PhotoImage(file="bathroom.png")
botao1 = Button(text='Banheiro', command = lambda: comando(1))
botao1.config(image=ico1, highlightthickness = 0, bd=0)
botao1.place(x=50,y=90)

#Fome

texto2 = Label(text='Fome', fg='green')
texto2.place(x=200,y=70)

ico2 = ImageTk.PhotoImage(file="food.png")
botao2 = Button(text='Fome', command = lambda: comando(2))
botao2.config(image=ico2, highlightthickness = 0, bd=0)
botao2.place(x=200,y=90)

#Socorro

texto3 = Label(text='Socorro', fg='red')
texto3.place(x=350,y=70)

ico3 = ImageTk.PhotoImage(file="help.png")
botao3 = Button(text='Socorro', command = lambda: comando(3))
botao3.config(image=ico3, highlightthickness = 0, bd=0)
botao3.place(x=350,y=90)

#Sono

texto4 = Label(text='Sono', fg='purple')
texto4.place(x=500,y=70)

ico4 = ImageTk.PhotoImage(file="sleep.png")
botao4 = Button(text='Sono', command = lambda: comando(4))
botao4.config(image=ico4, highlightthickness = 0, bd=0)
botao4.place(x=500,y=90)

janela.mainloop()