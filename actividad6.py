# 1. Pedir la temperatura al usuario
temp_input = input("Ingrese la temperatura actual en °C: ")

# Validación: Asegura que la entrada sea un número (permite negativos y decimales)
while not temp_input.replace('.', '', 1).replace('-', '', 1).isdigit():
    print("Entrada no válida. Por favor, ingrese un número.")
    temp_input = input("Ingrese la temperatura actual en °C: ")

# Convertir la entrada a número flotante (decimal)
temperatura = float(temp_input)

# 2. Evaluar la temperatura y dar sugerencias
if temperatura >= 30:
    print("Hace mucho calor. ¡Te sugiero un helado!")
elif temperatura >= 20: # Esto cubre el rango entre 20 y 29.9
    print("El clima está agradable. Te sugiero una limonada.")
else: # Esto cubre cualquier valor menor a 20
    print("Está algo fresco. Te sugiero un café.")