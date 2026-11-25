# adivinar numero entre 1-20 y indicar si es mayor o menor en cada intento
import random # Importamos el módulo random para generar un número aleatorio
numero_secreto = random.randint(1, 20) # Generamos un número aleatorio entre 1 y 20
intentos = 0 # Inicializamos el contador de intentos
while True: # Iniciamos un bucle infinito
    intento = int(input("Adivina el número entre 1 y 20: ")) # Pedimos al usuario que ingrese un número
    intentos += 1 # Incrementamos el contador de intentos
    if intento < numero_secreto: # Verificamos si el intento es menor al número secreto
        print("Demasiado bajo.") # Imprimimos un mensaje indicando que el intento es demasiado bajo
    elif intento > numero_secreto: # Verificamos si el intento es mayor al número secreto
        print("Demasiado alto.") # Imprimimos un mensaje indicando que el intento es demasiado alto
    else: # Si el intento es igual al número secreto
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.") # Imprimimos un mensaje de felicitación con el número de intentos
        break # Salimos del bucle