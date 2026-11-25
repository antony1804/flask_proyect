numeros = [5, 3, 8, 3, 5, 1, 8]

# 1. Eliminar duplicados con set() y ordenar con sorted()
unicos = sorted(set(numeros))

# 2. Imprimir resultados
print("Lista ordenada sin duplicados:", unicos)
print("Longitud:", len(unicos))
print("Mínimo:", min(unicos))
print("Máximo:", max(unicos))