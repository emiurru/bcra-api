import requests

#Toekn de acceso obtenido de https://estadisticasbcra.com/api/registracion
token = 'tu_token_AQUI'

headers = {
    'Authorization': f'Bearer {token}'
}

#URL de la base de datos que quieran acceder
url = 'https://api.estadisticasbcra.com/usd'

response = requests.get(url, headers=headers)

# Manejo de errores
try:   
    data = response.json()
    print(data)
except:
    # Manejar los errores
    print("Error al obtener acceso:", response.status_code, response.text)