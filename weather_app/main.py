import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import json
from datetime import datetime
import pytz
import pycountry_convert as pc
import os


def informacao():
    chave = '4079b0973de0b47cf143d444d6bde8a9'
    cidade = e_local.get()
    api_link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}"

    # chamando API com request
    r = requests.get(api_link)

    #converter os dados presentes
    dados = r.json()

    print(dados)
    print("*"*45)

    #cidade, pais e horas
    pais_codigo = dados['sys']['country']

    #fuso
    zona_fuso = pytz.country_timezones[pais_codigo]

    #pais
    pais = pytz.country_names[pais_codigo]

    #data
    zona = pytz.timezone(zona_fuso[0])
    zona_horas = datetime.now(zona)
    zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")

    #tempo
    tempo = dados['main']['temp']
    pressao = dados['main']['pressure']
    humidade = dados['main']['humidity']
    velocidade_vento = dados['wind']['speed']
    descricao = dados['weather'][0]['description']

    # mudar informações
    def pais_para_continente(n):
        pais_alpha = pc.country_name_to_country_alpha2(n)
        pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
        pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continente_codigo)
        
        return pais_continente_nome

    continente = pais_para_continente(pais)



    country_code = pc.country_name_to_country_alpha2("China", cn_name_format="default")

    continent_name = pc.country_alpha2_to_continent_code(country_code)
    
    #passar informaçao nas labels
    l_cidade["text"] = cidade + " - " + pais + " / " + continente
    l_data["text"] = zona_horas
    l_humidade["text"] = humidade
    l_humidade_texto["text"] = "Humidade"
    l_pressao["text"] = "Pressao : "+str(pressao)
    l_porcentagem["text"] = "%"
    l_velocidade["text"] = "Velocidade do vento: "+str(velocidade_vento)
    l_descricao["text"] = descricao

    #logica para trocar o fundo
    zona_periodo = datetime.now(zona)
    zona_periodo = zona_periodo.strftime("%H")

    global imagem
    
    zona_periodo = int(zona_periodo)
    if zona_periodo < 6:
        caminho_imagem = os.path.join(os.path.dirname(__file__), "images", "noite.png")
        fundo = fundo_noite
    elif 6 <= zona_periodo < 12:
        caminho_imagem = os.path.join(os.path.dirname(__file__), "images", "dia.png")
        fundo = fundo_dia
    elif 12 <= zona_periodo < 18:
        caminho_imagem = os.path.join(os.path.dirname(__file__), "images", "tarde.png")
        fundo = fundo_tarde
    else:
        caminho_imagem = os.path.join(os.path.dirname(__file__), "images", "noite.png")
        fundo = fundo_noite

    imagem = Image.open(caminho_imagem)
    imagem = ImageTk.PhotoImage(imagem)
    l_icon = Label(frame_corpo, image=imagem, bg=fundo)
    l_icon.place(x=200, y=50)

    #labels de fundo
    janela.configure(bg=fundo)
    frame_top.configure(bg=fundo)
    frame_corpo.configure(bg=fundo)

    l_cidade["bg"] = fundo
    l_data["bg"] = fundo
    l_humidade["bg"] = fundo
    l_humidade_texto["bg"] = fundo
    l_pressao["bg"] = fundo
    l_porcentagem["bg"] = fundo
    l_velocidade["bg"] = fundo
    l_descricao["bg"] = fundo

        

    




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
b_ver = Button(frame_top, command=informacao, text="Ver clima", bg=co1, fg=co2, font=("Ivy 9 bold"), relief="raised", overrelief=RIDGE)
b_ver.place(x=250, y=10)

#configurando frame corpo

l_cidade = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Ivy 11 bold"))
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Ivy 10 bold"))
l_data.place(x=10, y=35)

l_humidade = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Ivy 45 bold"))
l_humidade.place(x=10, y=70)

l_porcentagem = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Ivy 10 bold"))
l_porcentagem.place(x=85, y=80)

l_humidade_texto = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Ivy 10 bold"))
l_humidade_texto.place(x=85, y=110)

l_pressao = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Ivy 10 bold"))
l_pressao.place(x=10, y=150)

l_velocidade = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Ivy 10 bold"))
l_velocidade.place(x=10, y=170)


l_descricao = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=co1, font=("Ivy 10 bold"))
l_descricao.place(x=10, y=190)

janela.mainloop()
