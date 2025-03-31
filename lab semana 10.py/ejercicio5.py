#Modulo para conversion de unidades

# conversor.py

# Función para convertir kilómetros a millas
def kilometros_a_millas(kilometros):
    return kilometros * 0.621371

# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Función para convertir litros a galones
def litros_a_galones(litros):
    return litros * 0.264172





# programa_principal.py
import ejercicio5

def mostrar_menu():
    print("\nConversor de Unidades")
    print("1. Kilómetros a Millas")
    print("2. Celsius a Fahrenheit")
    print("3. Litros a Galones")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            kilometros = float(input("Ingresa la cantidad de kilómetros: "))
            millas = ejercicio5.kilometros_a_millas(kilometros)
            print(f"{kilometros} kilómetros son {millas} millas.")

        elif opcion == '2':
            celsius = float(input("Ingresa la temperatura en Celsius: "))
            fahrenheit = ejercicio5.celsius_a_fahrenheit(celsius)
            print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

        elif opcion == '3':
            litros = float(input("Ingresa la cantidad de litros: "))
            galones = ejercicio5.litros_a_galones(litros)
            print(f"{litros} litros son {galones} galones.")

        elif opcion == '4':
            print("¡Gracias por usar el conversor de unidades!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
