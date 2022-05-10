import requests
import geocoder 

# Chave api da pagina openweathermap.org
API_KEY = "YOURAPIKEY"

# Chave api da pagina Bing Portal
API_KEY_BING_PORTAL = 'YOURAPIKEY'

# Url que iremos fazer a requisição
BASE_URL= "http://api.openweathermap.org/data/2.5/weather"

# Parametro na URL para que o resultado seja em PT-BR
LANG = 'pt-br'

# Parametro na URL para que o resultado seja na unidade de medida 'Metric'
METRIC = 'metric'

city = input("Enter a city name: ")

# Modulo que com base no nome da cidade pega a longitude e a latitude 
g = geocoder.bing(f'{city}', key=f'{API_KEY_BING_PORTAL}')
results = g.json

lat  = results['lat']
lng = results['lng']
country_city = results['city']

# Irá usar a longitude e a latitude para enviar uma requisição e pegar os dados que precisamos
request_url = F"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={API_KEY}&lang={LANG}&units={METRIC}"
response = requests.get(request_url)
data = response.json()

# Separando as informações que quero exibir da variavel 'data' que está em formato .json
weather = data['weather']
current_temperature = data['main']['temp'] 
temp_min= data['main']['temp_min'] 
temp_max = data['main']['temp_max'] 
country = data['sys']['country']
feels_like = data['main']['feels_like']
wind = data['wind']['speed'] 

print(data)
print(weather)
print('*'*100)
print(f'{country_city}-{country}')
print(f'Temperatura Atual: {current_temperature:.0f}° graus')
print(f'Sensação térmica: {feels_like:.0f}° graus')
print(f'Temperatura Minima: {temp_min:.0f}° graus')
print(f'Temperatura Maxima: {temp_max:.0f}° graus')

print('*'*100)
print('Vento')
print(f'velocidade: {wind}km')




