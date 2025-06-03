# Importamos los módulos necesarios desde la carpeta 'Librerias'
import Librerias.Operaciones as oper  # Módulo que contiene funciones relacionadas con cálculos
import Librerias.salir as salir       # Módulo que gestiona la salida del programa
import Librerias.reportar as repor    # Módulo encargado de mostrar reportes

# Definimos la función 'menu' que muestra el menú principal y pide al usuario una opción
def menu():
    print("=== Menú Principal ===")
    print("""
    1. Calcular
    2. Reportar
    3. Salir
    """)
    while True:
        op =  input("Qué opción necesita:\t")  # Se solicita al usuario que elija una opción
        if op in ("1", "2", "3"):  # Validación de entrada
            return int(op)        # Si es válida, se convierte a entero y se retorna
        else:
            print("Ingrese una opción válida")  # Si no es válida, se muestra un mensaje de error
            print("\n=== Menú Principal ===")   # Y se vuelve a mostrar el menú
            print("1. Calcular")
            print("2. Reportar")
            print("3. Salir")

# Función principal que controla el programa
def ejecutar():
    while True:           # Bucle infinito hasta que el usuario decida salir
        opcion = menu()   # Se llama al menú para obtener una opción válida
        if opcion == 1:
            oper.calcular()     # Llama a la función 'calcular' del módulo 'Operaciones'
        elif opcion == 2:
            repor.reportar()    # Llama a la función 'reportar' del módulo 'reportar'
        elif opcion == 3:
            salir.salir()       # Llama a la función 'salir' del módulo 'salir'
            break               # Rompe el bucle para terminar el programa
        else:
            print("Ingrese una opción válida")  # Esta línea es redundante, pero está como seguridad extra

# Iniciamos el programa llamando a la función 'ejecutar'
ejecutar()
