#Generar y analizar histogramas de datos

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def generar_datos(n, media, desviacion_estandar):
    # Genera una muestra de datos aleatorios con distribución normal
    return np.random.normal(media, desviacion_estandar, n)

def analizar_datos(datos):
    # Cálculos estadísticos básicos
    media = np.mean(datos)
    mediana = np.median(datos)
    desviacion_estandar = np.std(datos)
    moda = stats.mode(datos)[0][0]
    rango = np.ptp(datos)  # Rango (valor máximo - valor mínimo)
    percentiles = np.percentile(datos, [25, 50, 75])  # 25%, 50% (mediana), 75%
    
    print(f"Análisis de los datos:")
    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Desviación estándar: {desviacion_estandar:.2f}")
    print(f"Moda: {moda:.2f}")
    print(f"Rango: {rango:.2f}")
    print(f"Percentiles (25%, 50%, 75%): {percentiles}")
    
def graficar_histograma(datos, bins=10):
    # Genera un histograma de los datos
    plt.figure(figsize=(8, 6))
    plt.hist(datos, bins=bins, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title("Histograma de Datos")
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.show()

def main():
    # Parámetros de ejemplo
    n = int(input("Ingresa el número de datos a generar: "))
    media = float(input("Ingresa la media de los datos: "))
    desviacion_estandar = float(input("Ingresa la desviación estándar de los datos: "))
    
    # Generación de datos
    datos = generar_datos(n, media, desviacion_estandar)
    
    # Análisis de los datos
    analizar_datos(datos)
    
    # Graficar histograma
    graficar_histograma(datos, bins=20)

if __name__ == "__main__":
    main()
