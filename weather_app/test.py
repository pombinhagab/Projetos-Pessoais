import requests
import json
import datetime
import pytz

chave = '4079b0973de0b47cf143d444d6bde8a9'
cidade = 'Lisboa'
api_link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}"

# chamando API com request
r = requests.get(api_link)

#converter os dados presentes
dados = r.json()

print(dados)
print("*"*45)

#cidade, pais e horas
pais_codigo = dados['sys']['country']
print(pais_codigo)

#fuso
zona_fuso = pytz.country_timezones[pais_codigo]

#pais
pais = pytz.country_names[pais_codigo]

#data
zona = pytz.timezone(zona_fuso[0])
zona_horas = datetime.now(zona)
print(zona)
