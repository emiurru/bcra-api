import requests

#Toekn de acceso obtenido de https://estadisticasbcra.com/api/registracion

token = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzk1Mzg3MjcsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJlbWlsaWFub0Bsb25nY3JlZHNhLmNvbS5hciJ9.UnQKBvKZa4ZAskJnOrR03guJ4sF_ETBLh_71a8hqvHL57LllmnyFyO_BXGjdzReSyjdlAKdjp8HfVL5W5qi8Qg'

headers = {
    'Authorization': f'Bearer {token}'
}

#URL de la base de datos que quieran acceder
url = 'https://api.estadisticasbcra.com/usd'

response = requests.get(url, headers=headers)

# Verificar si la solicitud fue exitosa
try:   
    data = response.json()
    print(data)
except:
    # Manejar los errores
    print("Error al obtener acceso:", response.status_code, response.text)