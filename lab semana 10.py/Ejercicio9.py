#Implementacion de multiples paradigmas


# Modulo de calculadora con funciones de operaciones matemáticas
def calculadora():
 def sumar(a, b):
    return a + b

 def restar(a, b):
    return a - b

 def multiplicar(a, b):
    return a * b

 def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"






# Modulo de clases que definen una persona

def persona():
 class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.ocupacion}."





# Modulo con funciones adicionales, como generar números aleatorios

def utilidades():
 import random

 def generar_lista_aleatoria(tamaño):
    """Genera una lista de números aleatorios entre 1 y 100"""
    return [random.randint(1, 100) for _ in range(tamaño)]





import random
from Ejercicio9 import calculadora
from Ejercicio9 import persona
from Ejercicio9 import utilidades

# Paradigma imperativo: Uso de estructuras de control como condicionales y bucles
def menu_calculadora():
    print("\n--- Calculadora ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    while True:
        opcion = input("Seleccione una operación: ")
        if opcion == '1':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {calculadora.sumar(a, b)}")
        elif opcion == '2':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {calculadora.restar(a, b)}")
        elif opcion == '3':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {calculadora.multiplicar(a, b)}")
        elif opcion == '4':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {calculadora.dividir(a, b)}")
        elif opcion == '5':
            print("Saliendo de la calculadora.")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Paradigma estructurado: Separación en funciones
def crear_persona():
    print("\n--- Crear Persona ---")
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad: "))
    ocupacion = input("Ingrese la ocupación: ")
    
    persona_obj = persona.Persona(nombre, edad, ocupacion)
    print(persona_obj.presentarse())

def generar_lista_aleatoria():
    print("\n--- Generador de lista aleatoria ---")
    tamaño = int(input("Ingrese el tamaño de la lista: "))
    lista = utilidades.generar_lista_aleatoria(tamaño)
    print("Lista generada:", lista)
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)

# Paradigma orientado a objetos: Uso de clases y objetos
def crear_objeto_persona():
    print("\n--- Crear y mostrar información de persona ---")
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad: "))
    ocupacion = input("Ingrese la ocupación: ")
    persona_obj = persona.Persona(nombre, edad, ocupacion)
    print(persona_obj.presentarse())
    return persona_obj

# Función principal para interactuar con el usuario
def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Calculadora")
        print("2. Crear Persona y Presentarse")
        print("3. Generar lista aleatoria y ordenarla")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            menu_calculadora()
        elif opcion == '2':
            crear_persona()
        elif opcion == '3':
            generar_lista_aleatoria()
        elif opcion == '4':
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
