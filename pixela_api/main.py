import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "ivanmoracar"
TOKEN = "poiuytre182"
GRAPHID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Crear usuario (ya comentado en tu código)
# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph__config = {
    "id": GRAPHID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Crear gráfico (comentado en tu código)
# response = requests.post(url=graph_endpoint, json=graph__config, headers=headers)
# response.raise_for_status()
# print(response.text)

# Agregar un píxel
today = datetime.now().strftime("%Y%m%d")
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

pixel_config = {
    "date": today,
    "quantity": "3"
}

# response = requests.post(url=graph_endpoint, json=pixel_config, headers=headers)
# response.raise_for_status()
# print(response.text)


# https://pixe.la/v1/users/ivanmoracar/graphs/graph1/20241205


update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today}"

new_pixel_config = {
    "quantity": "3"
}

# response = requests.put(url=update_graph_endpoint, json=new_pixel_config, headers=headers)
# response.raise_for_status()
# print(response.text)


# Eliminar un píxel

delete_pixel_endpoint = f"{graph_endpoint}/{today}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
response.raise_for_status()
print(response.text)