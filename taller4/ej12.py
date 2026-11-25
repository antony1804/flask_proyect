try:
    a = float(input("Primer número: ")) #pedimos los dos numeros
    b = float(input("Segundo número: "))
    resultado = a / b
except ValueError:
    print("Debes ingresar números válidos.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
else:
    print("Resultado:", resultado)
finally:
    print("Operación finalizada")