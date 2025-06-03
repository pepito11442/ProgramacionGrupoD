# Inicializamos contadores para cada categoría de decibeles
cat_A = 0
cat_B = 0
cat_C = 0
cat_D = 0
cat_E = 0

# Listas para guardar los valores monetarios
plata = []              # Almacena los montos ingresados en dólares
cambio_de_dolar = []    # Almacena los montos convertidos a soles antes de penalidad
penalidades = []        # Almacena los montos en soles luego de aplicar la penalidad

# Función principal para realizar los cálculos
def calcular():
    global plata, cat_A, cat_B, cat_C, cat_D, cat_E, cambio_de_dolar, penalidades
    
    # Imprimimos las categorías de penalidad según los decibeles
    print("="*50)
    print("=========== PENALIDADES ===========")
    print("A | De 0 a 60 decibeles     | 5% de penalidad")
    print("B | De 61 a 100 decibeles   | 7% de penalidad")
    print("C | De 101 a 149 decibeles  | 9% de penalidad")
    print("D | De 150 a 200 decibeles  | 12% de penalidad")
    print("E | De 200 a más decibeles  | 15% de penalidad")

    # Pedimos datos al usuario
    decibeles = float(input("\nIngrese la cantidad de decibeles: "))
    dinero = float(input("\nIngrese la cantidad en dólares: "))
    cambio = float(input("\nIngrese el cambio de dólar a sol: "))

    plata.append(dinero)  # Guardamos el monto en dólares

    # Asignamos categoría y penalidad según el rango de decibeles
    if decibeles <= 60:
        print("\nSu categoría asignada es A")
        penalidad = 0.05
        cat_A += 1
    elif 61 <= decibeles <= 100:
        print("\nSu categoría asignada es B")
        penalidad = 0.07
        cat_B += 1
    elif 101 <= decibeles <= 149:
        print("\nSu categoría asignada es C")
        penalidad = 0.09
        cat_C += 1
    elif 150 <= decibeles <= 200:
        print("\nSu categoría asignada es D")
        penalidad = 0.12
        cat_D += 1
    else:
        print("\nSu categoría asignada es E")
        penalidad = 0.15
        cat_E += 1

    # Mostramos los valores ingresados
    print("\nSu monto fue:", dinero)
    print("\nSu penalidad:", penalidad)
    print("\nSu tipo de cambio es:", cambio)

    # Conversión de dólares a soles
    dolares_a_soles = dinero * cambio
    dolares_round = round(dolares_a_soles, 2)

    # Cálculo de la penalidad en soles
    penalidad_cambio1 = dolares_a_soles * penalidad
    penalidad_cambio = dolares_a_soles - penalidad_cambio1
    penalidad_round = round(penalidad_cambio, 2)

    # Guardamos los resultados
    cambio_de_dolar.append(dolares_round)
    penalidades.append(penalidad_round)
