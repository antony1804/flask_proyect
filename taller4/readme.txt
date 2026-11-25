# Gestor de Gastos Personales

## Planteamiento del problema
Aplicación de consola para registrar gastos diarios por categoría, consultar el historial y calcular el total gastado en cada categoría de forma persistente.

## Diseño del programa
El sistema se divide en 6 funciones principales y almacena los datos en `gastos.txt`:

- `cargar()`: lee el archivo `gastos.txt` al iniciar y recupera los registros previos.
- `guardar(gastos)`: escribe la lista actualizada de gastos en el archivo de texto.
- `agregar_gasto(gastos)`: solicita categoría y monto, valida que los datos sean correctos y guarda el registro.
- `listar_gastos(gastos)`: muestra todos los gastos registrados en consola.
- `total_por_categoria(gastos)`: agrupa los gastos en un diccionario y muestra la suma total por categoría.
- `menu()`: muestra las opciones disponibles y controla la navegación del usuario.

## Cómo ejecutarlo
1. Asegúrate de tener Python 3 instalado.
2. Abre la carpeta del proyecto en VS Code.
3. Ejecuta el archivo principal desde la terminal:
   ```bash
   python gestor_gastos.py