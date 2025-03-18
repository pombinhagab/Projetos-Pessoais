import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


##Cores
co0 = "#444466" #Preta
co1 = "#feffff" #Branca
co2 = "#6f9fdb" #Azul

fundo_dia = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb86d"
fundo = fundo_dia

janela = Tk()
janela.title = ("")
janela.geometry("320x350")
janela.configure(bg=fundo)
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=159)

#Frames

frame_top = Frame(janela, width=320, height=50, bg=co1,pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo,pady=12, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

#configurando frame_top

e_local = Entry(frame_top, width=20, justify="left", font=("", 14), highlightthickness=1, relief="solid")
e_local.place(x=15, y=10)
b_ver = Button(frame_top, text="Ver clima", bg=co1, fg=co2, font=("Ivy 9 bold"), relief="raised", overrelief=RIDGE)
b_ver.place(x=250, y=10)

#configurando frame corpo

l_cidade = Label(frame_corpo, text="Juiz de Fora - Brasil / América do Sul", anchor="center", bg=fundo, fg=co1, font=("Ivy 11 bold"))
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text="15 03 2025 | 07:35 AM", anchor="center", bg=fundo, fg=co1, font=("Ivy 10 bold"))
l_data.place(x=10, y=35)

l_humidade = Label(frame_corpo, text="84", anchor="center", bg=fundo, fg=co1, font=("Ivy 45 bold"))
l_humidade.place(x=10, y=70)

l_porcentagem = Label(frame_corpo, text="%", anchor="center", bg=fundo, fg=co1, font=("Ivy 10 bold"))
l_porcentagem.place(x=85, y=80)

l_humidade_texto = Label(frame_corpo, text="Humidade", anchor="center", bg=fundo, fg=co1, font=("Ivy 10 bold"))
l_humidade_texto.place(x=85, y=110)

l_pressao = Label(frame_corpo, text="Pressão: 1000", anchor="center", bg=fundo, fg=co1, font=("Ivy 10 bold"))
l_pressao.place(x=10, y=150)

l_velocidade = Label(frame_corpo, text="Velocidade do vento: 4SWM", anchor="center", bg=fundo, fg=co1, font=("Ivy 10 bold"))
l_velocidade.place(x=10, y=170)


l_descricao = Label(frame_corpo, text="Nublado", anchor="center", bg=fundo, fg=co1, font=("Ivy 10 bold"))
l_descricao.place(x=10, y=190)

imagem = Image.open("images/dia.png")
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_corpo, image=imagem, bg=fundo)
l_icon.place(x=200, y=50)


janela.mainloop()
