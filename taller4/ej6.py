nota = int(input("Ingrese la nota del estudiante (0-100): ")) # Pedimos al usuario que ingrese la nota del estudiante
if nota >= 90: # Verificamos si la nota es mayor o igual a 90
    print("A") # Imprimimos A si la nota es mayor o igual a 90
elif nota >= 80: # Verificamos si la nota es mayor o igual a    80
    print("B") # Imprimimos B si la nota es mayor o igual a 80          
elif nota >= 70: # Verificamos si la nota es mayor o igual a 70
    print("C") # Imprimimos C si la nota es mayor o igual a 70
elif nota >= 60: # Verificamos si la nota es mayor o igual a 60
    print("D") # Imprimimos D si la nota es mayor o igual a 60
else: # Si la nota es menor a 60
    print("F") # Imprimimos F si la nota es menor a 60
