# Solicitar el nombre del curso
curso = input("Ingrese el nombre del curso: ")

# Solicitar la cantidad de notas
cantidad_notas = int(input("Ingrese la cantidad de notas: "))

suma_notas = 0

# Ciclo for para ingresar cada nota
for i in range(cantidad_notas):
    nota = int(input(f"Ingrese la nota {i + 1}: "))
    suma_notas += nota

# Calcular el promedio
promedio = suma_notas / cantidad_notas

# Mostrar el resultado
print(f"El promedio del curso {curso} es: {promedio}")
