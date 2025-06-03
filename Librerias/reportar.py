# Se importa un módulo personalizado llamado 'Operaciones' desde la carpeta 'Librerias'
# y se le asigna un alias 'oper' para usarlo más fácilmente.
import Librerias.Operaciones as oper

# Se define una función llamada 'reportar', que mostrará un submenú con diferentes reportes.
def reportar():
    while True:  # Bucle infinito para que el menú se repita hasta que el usuario elija salir.
        print("==== Sub Menu Reportes")
        print("1. Mostrar cambios de dolar a sol")
        print("2. Mostrar penalidads de dolar a sol")
        print("3. Reporte de decibelios")
        print("4. Salir")
        
        # Solicita al usuario que ingrese una opción y la convierte a entero
        opcion = int(input("Opcion a elegir:\t"))

        # Se usa la estructura 'match-case' (parecida a switch en otros lenguajes) para decidir qué hacer.
        match opcion:
            case 1:
                # Muestra el valor de la variable 'cambio_de_dolar' del módulo 'oper'.
                print("El cambio fue:", oper.cambio_de_dolar, "Soles")
            case 2:
                # Muestra el valor de la variable 'penalidades' del módulo 'oper'.
                print("La penalidad aplicada fue:", oper.penalidades, "Soles")
            case 3:
                # Muestra los valores de decibelios por categoría (A a E) desde el módulo 'oper'.
                print("Decibelios cat A:", oper.cat_A)
                print("Decibelios cat B:", oper.cat_B)
                print("Decibelios cat C:", oper.cat_C)
                print("Decibelios cat D:", oper.cat_D)
                print("Decibelios cat E:", oper.cat_E)
            case 4:
                # Sale del bucle y termina la función.
                break
