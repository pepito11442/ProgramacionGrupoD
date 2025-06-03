import Librerias.Operaciones as oper
def reportar():
    while True:
        print("==== Sub Menu Reportes")
        print("1. Mostrar cambios de dolar a sol")
        print("2. Mostrar penalidads de dolar a sol")
        print("3. Reporte de decibelios")
        print("4. Salir")
        opcion = int(input("Opcion a elegir:\t"))
        match opcion:
            case 1:
                print("El cambio fue:", oper.cambio_de_dolar, "Soles")
            case 2:
                print("La penalidad aplicada fue:", oper.penalidades, "Soles")
            case 3:
                print("Decibelios cat A:", oper.cat_A)
                print("Decibelios cat B:", oper.cat_B)
                print("Decibelios cat C:", oper.cat_C)
                print("Decibelios cat D:", oper.cat_D)
                print("Decibelios cat E:", oper.cat_E)
            case 4:
                break