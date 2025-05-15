import requests
import numpy as np
import statistics as stats
 
# 1. Configuración inicial
URL_API = "https://pokeapi.co/api/v2/pokemon"
CANTIDAD_POKEMON = 150  # Puedes cambiar este número si quieres más Pokémon
 
# 2. Función para obtener datos de Pokémon
def obtener_datos_pokemon(cantidad):
    datos = {
        'height': [],
        'weight': [],
        'base_experience': []
    }
    for id_pokemon in range(1, cantidad + 1):
        respuesta = requests.get(f"{URL_API}/{id_pokemon}")
        if respuesta.status_code == 200:
            pokemon = respuesta.json()
            datos['height'].append(pokemon.get('height', 0))
            datos['weight'].append(pokemon.get('weight', 0))
            datos['base_experience'].append(pokemon.get('base_experience', 0))
            print(f"Datos obtenidos de {pokemon['name']}")
        else:
            print(f"No se pudo obtener el Pokémon con ID {id_pokemon}")
    return datos
 
# 3. Función para análisis estadístico
def analisis_estadistico(datos):
    analisis = {}
    for categoria, valores in datos.items():
        analisis[categoria] = {
            'media': np.mean(valores),
            'mediana': np.median(valores),
            'moda': stats.mode(valores),
            'desviacion_estandar': np.std(valores),
            'minimo': np.min(valores),
            'maximo': np.max(valores),
            'cantidad': len(valores)
        }
    return analisis
 
# 4. Ejecución principal
if __name__ == "__main__":
    print("Iniciando obtención de datos de Pokémon...")
    datos_pokemon = obtener_datos_pokemon(CANTIDAD_POKEMON)
 
    if datos_pokemon:
        resultados = analisis_estadistico(datos_pokemon)
        print("\nResultados del Análisis Estadístico:")
        for categoria, estadisticas in resultados.items():
            print(f"\n{categoria.capitalize()}:")
            for clave, valor in estadisticas.items():
                print(f"  {clave.capitalize()}: {valor}")
 
    else:
        print("No se pudieron obtener datos de Pokémon.")