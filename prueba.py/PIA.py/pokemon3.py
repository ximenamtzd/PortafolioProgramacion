import json
import csv
import re
import os
import statistics
import numpy as np
from openpyxl import load_workbook

# Expresión regular para validar nombres de Pokémon y habilidades
regex_nombre = re.compile(r"^[a-zA-Z\-]+$")
regex_tipo = re.compile(r"^[a-z]+$")
regex_habilidad = re.compile(r"^[a-z\-]+$")

# Ruta de archivos
archivo_json = "pokemones.json"
archivo_csv = "pokemones.csv"
archivo_excel = "pokemones.xlsx"

# Leer datos desde JSON
def leer_json():
    if not os.path.exists(archivo_json):
        print("Archivo JSON no encontrado.")
        return []
    with open(archivo_json, "r") as f:
        return json.load(f)

# Validar datos
def validar_datos(pokemones):
    validos = []
    for p in pokemones:
        if (
            regex_nombre.fullmatch(p["nombre"]) and
            all(regex_tipo.fullmatch(t) for t in p["tipos"]) and
            all(regex_habilidad.fullmatch(h) for h in p["habilidades"])
        ):
            validos.append(p)
    return validos

# Análisis de tipos y habilidades


def analizar_datos(pokemones):
    cantidad_tipos = [len(p["tipos"]) for p in pokemones]
    cantidad_habilidades = [len(p["habilidades"]) for p in pokemones]

    print("\n--- Análisis Estadístico ---")
    print(f"Número de Pokémon analizados: {len(pokemones)}")

    if cantidad_tipos:
        print("\nTipos:")
        print(f"  Media: {statistics.mean(cantidad_tipos):.2f}")
        print(f"  Mediana: {statistics.median(cantidad_tipos)}")
        if len(cantidad_tipos) > 1:
            print(f"  Moda: {statistics.mode(cantidad_tipos)}")
            print(f"  Desviación estándar: {statistics.stdev(cantidad_tipos):.2f}")
        else:
            print("  No se puede calcular moda ni desviación estándar con un solo dato.")

    if cantidad_habilidades:
        print("\nHabilidades:")
        print(f"  Media: {np.mean(cantidad_habilidades):.2f}")
        print(f"  Mediana: {np.median(cantidad_habilidades)}")
        if len(cantidad_habilidades) > 1:
            print(f"  Moda: {statistics.mode(cantidad_habilidades)}")
            print(f"  Desviación estándar: {np.std(cantidad_habilidades):.2f}")
        else:
            print("  No se puede calcular moda ni desviación estándar con un solo dato.")


    # Preparar estructura para visualización (ejemplo simple)
    datos_visuales = [{
        "nombre": p["nombre"],
        "n_tipos": len(p["tipos"]),
        "n_habilidades": len(p["habilidades"])
    } for p in pokemones]
    
    return datos_visuales

# Ejecutar flujo completo
if __name__ == "__main__":
    pokemones = leer_json()
    if not pokemones:
        print("No se encontraron datos válidos.")
    else:
        pokemones_validos = validar_datos(pokemones)
        datos_visualizacion = analizar_datos(pokemones_validos)
        
        print("\nDatos preparados para visualización:")
        for d in datos_visualizacion:
            print(d)
