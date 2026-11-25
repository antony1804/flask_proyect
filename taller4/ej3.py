


año = int(input("Ingrese un año: ")) # Pedimos al usuario que ingrese un año
# Año bisiesto
es_bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0) # Verificamos si el año es bisiesto usando las reglas del calendario gregoriano
print(es_bisiesto) # Imprimimos True si el año es bisiesto, False en caso contrario
