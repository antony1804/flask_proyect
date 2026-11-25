ARCHIVO = "gastos.txt"  # Nombre del archivo donde se guardará todo


def cargar():
    """Lee los gastos guardados en el archivo al iniciar el programa."""
    gastos = []
    try:
        with open(ARCHIVO, "r") as f:
            for linea in f:
                # Divide cada línea usando la coma: "Comida,15.5" -> ["Comida", "15.5"]
                categoria, monto = linea.strip().split(",")
                gastos.append((categoria, float(monto)))  # Guarda como tupla (categoría, número)
    except FileNotFoundError:
        pass  # Si el archivo aún no existe (primera vez), no da error y devuelve lista vacía
    return gastos


def guardar(gastos):
    """Guarda toda la lista de gastos en el archivo de texto."""
    with open(ARCHIVO, "w") as f:
        for categoria, monto in gastos:
            f.write(f"{categoria},{monto}\n")  # Escribe cada gasto separado por coma


def agregar_gasto(gastos):
    """Pide categoría y monto, valida los datos y los agrega a la lista."""
    categoria = input("Categoría (ej. Comida, Transporte): ").strip().capitalize()
    if not categoria:  # Valida que no quede en blanco
        print("Error: La categoría no puede estar vacía.")
        return

    try:
        monto = float(input("Monto: "))  # Intenta convertir lo escrito a número
        if monto <= 0:  # Valida que sea un número positivo
            print("Error: El monto debe ser mayor a cero.")
            return
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return

    gastos.append((categoria, monto))  # Agrega el gasto como una tupla a la lista
    guardar(gastos)  # Actualiza el archivo inmediatamente
    print("Gasto guardado correctamente.")


def listar_gastos(gastos):
    """Muestra todos los gastos registrados uno por uno."""
    if not gastos:  # Revisa si la lista está vacía
        print("No hay gastos registrados.")
        return

    print("\n--- Lista de Gastos ---")
    for categoria, monto in gastos:
        print(f"- {categoria}: ${monto:.2f}")


def total_por_categoria(gastos):
    """Agrupa y suma los gastos usando un diccionario."""
    if not gastos:
        print("No hay gastos para calcular.")
        return

    totales = {}  # Diccionario para acumular: {"Comida": 30.0, "Ocio": 15.0}
    for categoria, monto in gastos:
        # .get() busca la categoría; si no existe aún, empieza en 0 y le suma el monto
        totales[categoria] = totales.get(categoria, 0) + monto

    print("\n--- Total por Categoría ---")
    for categoria, total in totales.items():
        print(f"{categoria}: ${total:.2f}")


def menu():
    """Controla el flujo principal del programa."""
    gastos = cargar()  # Carga los datos previos apenas arranca

    while True:
        print("\n1. Agregar gasto | 2. Listar gastos | 3. Total por categoría | 4. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_gasto(gastos)
        elif opcion == "2":
            listar_gastos(gastos)
        elif opcion == "3":
            total_por_categoria(gastos)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Punto de entrada del programa
menu()