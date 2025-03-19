import requests
import json
from datetime import datetime
import pytz
import pycountry_convert as pc


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

