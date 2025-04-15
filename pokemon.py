

import requests
import json

def obtener_datos_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos_pokemon = respuesta.json()
        return datos_pokemon
    else:
        print(f"Error: No se pudo obtener datos para {nombre_pokemon}")
        return None

nombre_pokemon = input("Ingrese el nombre del Pokémon a consultar: ")
datos_pokemon = obtener_datos_pokemon(nombre_pokemon)

if datos_pokemon:
    print(f"Información de {nombre_pokemon.title()}:")
    print(f"  Nombre: {datos_pokemon['name']}")
    print(f"  Tipos: {', '.join([tipo['type']['name'] for tipo in datos_pokemon['types']])}")
    print(f"  Habilidades: {', '.join([habilidad['ability']['name'] for habilidad in datos_pokemon['abilities']])}")


