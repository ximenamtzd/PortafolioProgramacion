import tkinter as tk

import requests
 
def obtener_datos_pokemon(nombre_pokemon):

    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"

    respuesta = requests.get(url)

    if respuesta.status_code == 200:

        datos = respuesta.json()

        nombre = datos["name"]

        tipos = [t["type"]["name"] for t in datos["types"]]

        habilidades = [h["ability"]["name"] for h in datos["abilities"]]

        return f"Nombre: {nombre}\nTipos: {', '.join(tipos)}\nHabilidades: {', '.join(habilidades)}"

    else:

        return f"No se encontró información para: {nombre_pokemon}"
 
#Función que se activa al hacer clic en el botón

def mostrar_info():

    nombre = entrada.get()

    info = obtener_datos_pokemon(nombre)

    resultado.config(text=info)
 
#Interfaz gráfica 

ventana = tk.Tk()

ventana.title("Consulta Pokémon")
 
tk.Label(ventana, text="Nombre del Pokémon:").pack(pady=5)

entrada = tk.Entry(ventana)

entrada.pack(pady=5)
 
tk.Button(ventana, text="Buscar", command=mostrar_info).pack(pady=5)

resultado = tk.Label(ventana, text="", justify="left")

resultado.pack(pady=10)
 
ventana.mainloop()
 
 