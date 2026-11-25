# tabla de multiplicar 
numero = int(input("Ingrese un número para ver su tabla de multiplicar: ")) # Pedimos al usuario que ingrese un número
print(f"Tabla de multiplicar del {numero}:") # Imprimimos un encabezado
for i in range(1, 11): # Iteramos del 1 al 10
    resultado = numero * i # Calculamos el resultado de la multiplicación
    print(f"{numero} x {i} = {resultado}") # Imprimimos el resultado de la multiplicación   