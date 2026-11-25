
inventario = {"manzanas": 10, "pan": 5} # crear el diccionario inicial {producto: cantidad}
inventario["leche"] = 8 #  agregar un producto nuevo
inventario["leche"] = 12 #  actualizar la cantidad del producto agregado
del inventario["pan"] # Eliminar otro producto del inventario
# Recorrer el inventario e imprimir cada par
for producto, cantidad in inventario.items():
    print(producto, cantidad)
