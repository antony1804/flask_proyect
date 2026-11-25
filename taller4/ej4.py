producto = input("Ingrese el nombre del producto: ") # Pedimos al usuario que ingrese el nombre del producto
precio = float(input("Ingrese el precio del producto: ")) # Pedimos al usuario que ingrese el precio del producto
cantidad = int(input("Ingrese la cantidad del producto: ")) # Pedimos al usuario que ingrese la cantidad del producto
costo_total = precio * cantidad # Calculamos el costo total del producto multiplicando el precio por la cantidad
print(f"El costo total de {cantidad} {producto}(s) es: ${costo_total:.2f}") # Imprimimos el costo total del producto con dos decimales