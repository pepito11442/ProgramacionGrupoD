import Librerias.Operaciones as oper
import Librerias.salir as salir
import Librerias.reportar as repor
def menu():
    print("=== Menú Principal ===")
    print("""
    1. Calcular
    2. Reportar
    3. Salir
    """)
    while True:
        op =  input("QUe opcion necesita:\t")
        if op in ("1", "2", "3"):
            return int(op)
        else:
            print("Ingrese una opcin valida")
            print("\n=== Menú Principal ===")
            print("1. Calcular")
            print("2. Reportar")
            print("3. Salir")


def ejecutar():
    while True:
        opcion = menu()
        if opcion == 1:
            oper.calcular()
        elif opcion == 2:
            repor.reportar()
        elif opcion == 3:
            salir.salir()
            break
        else:
            print("Ingrese una opcion valida")
ejecutar()