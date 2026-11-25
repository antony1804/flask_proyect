def estadisticas(lista):
    """Devuelve (mínimo, máximo, promedio) de una lista."""
    return min(lista), max(lista), sum(lista) / len(lista)
print(estadisticas([10, 20, 30])) # Tres pruebas
print(estadisticas([5, 2, 8, 1]))
print(estadisticas([4.5, 3.5, 4.0]))