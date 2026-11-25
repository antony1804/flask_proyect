import geometria  # Conecta con nuestro archivo geometria.py
import random  # Sirve para generar números al azar
from datetime import datetime  # Sirve para obtener la fecha y hora actual
# Usa las funciones que creamos en el otro archivo
print("Área del rectángulo:", geometria.area_rectangulo(5, 3))
print("Área del círculo:", geometria.area_circulo(4))
# Repite 5 veces el lanzamiento de un dado (números del 1 al 6)
for i in range(5):
    dado = random.randint(1, 6)  # Elige un número entero al azar entre 1 y 6
    print(f"Lanzamiento {i + 1}: {dado}")
# Muestra la fecha y hora exacta de este momento
print("Fecha y hora:", datetime.now())