
import requests

def traducir_libretranslate(texto, origen="en", destino="es"):
    url = "https://libretranslate.de/translate"
    datos = {
        "q": texto,
        "source": origen,
        "target": destino,
        "format": "text"
    }

    try:
        respuesta = requests.post(url, data=datos)
        respuesta.raise_for_status()
        return respuesta.json()["translatedText"]
    except Exception as error:
        print(f"⚠️ Error al traducir: {error}")
        return "(No se pudo traducir la sinopsis)"

def buscar_anime(nombre_anime):
    url = "https://api.jikan.moe/v4/anime"
    parametros = {"q": nombre_anime, "limit": 1}

    try:
        respuesta = requests.get(url, params=parametros)
        respuesta.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"❌ Error al conectar con la API de Jikan: {error}")
        return

    datos = respuesta.json()

    if not datos["data"]:
        print("❌ No se encontró ningún anime con ese nombre.")
        return

    anime = datos["data"][0]

    # Datos relevantes
    titulo = anime.get("title", "Desconocido")
    titulo_jp = anime.get("title_japanese", "Desconocido")
    url_anime = anime.get("url", "No disponible")
    fecha_emision = anime["aired"].get("from", "Desconocida")
    generos = ", ".join([g["name"] for g in anime.get("genres", [])])
    sinopsis_en = anime.get("synopsis", "Sin sinopsis disponible")

    # Traducción al español
    sinopsis_es = traducir_libretranslate(sinopsis_en)

    # Mostrar resultados
    print("\n📘 Información del Anime:")
    print(f"🎬 Título: {titulo}")
    print(f"🇯🇵 Título japonés: {titulo_jp}")
    print(f"📅 Fecha de emisión: {fecha_emision}")
    print(f"🎭 Géneros: {generos}")
    print(f"🔗 URL: {url_anime}")
    print(f"\n📖 Sinopsis en español:\n{sinopsis_es}")

# Ejecutar
if __name__ == "__main__":
    nombre = input("🔍 Escribe el nombre del anime que deseas buscar: ")
    buscar_anime(nombre)
