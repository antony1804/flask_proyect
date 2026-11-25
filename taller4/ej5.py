while True:
    edad = int(input("Ingrese su edad: ")) # Pedimos al usuario que ingrese su edad
    if edad > 0 and edad <= 120: # Verificamos si la edad ingresada es válida (entre 0 y 120)
        break # Si la edad es válida, salimos del bucle