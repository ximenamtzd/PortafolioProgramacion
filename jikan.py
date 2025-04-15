import requests

def buscar_anime(nombre_anime):
    url = f"https://api.jikan.moe/v4/anime"
    params = {"q": nombre_anime, "limit": 1}  # limit=1 para obtener solo el primero
    response = requests.get(url, params=params)

    if response.status_code == 200:
        datos = response.json()
        if datos["data"]:
            anime = datos["data"][0]
            print(f"Título: {anime['title']}")
            print(f" Fecha de emisión: {anime['aired']['from']}")
            print(f" Sinopsis: {anime['synopsis']}")
            print(f" URL: {anime['url']}")
        else:
            print("No se encontró ningún anime con ese nombre.")
    else:
        print(f"Error en la solicitud: {response.status_code}")

# Prueba
if __name__ == "__main__":
    nombre = input(" Escribe el nombre del anime que deseas buscar: ")
    buscar_anime(nombre)
