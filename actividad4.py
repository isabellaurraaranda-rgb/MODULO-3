# Listas de datos
nombres = ["Juan", "Ana", "Pedro", "Luis", "Maria"]
edades = [20, 22, 19, 21, 23]
calificaciones = [8, 6, -1, 9, 5]

suma_calificaciones = 0
contador_validas = 0

print("Listado de estudiantes:\n")

# Recorrer listas simultáneamente usando zip() y enumerate()
for indice, (nombre, edad, nota) in enumerate(zip(nombres, edades, calificaciones), start=1):
    print(f"{indice}. {nombre} - Edad: {edad} - Nota: {nota}")

    # Si el estudiante está retirado
    if nota == -1:
        print("Estudiante retirado. Programa finalizado.")
        break
    
    # Si la nota es menor a 6, se omite
    if nota < 6:
        continue

    # Si llega aquí, está aprobado (nota >= 6)
    print(f"Estudiante aprobado: {nombre} con nota {nota}")

    suma_calificaciones += nota
    contador_validas += 1

# Calcular promedio solo si hay notas válidas
if contador_validas > 0:
    promedio = suma_calificaciones / contador_validas
    print(f"\nPromedio de calificaciones válidas: {promedio}")
else:
    print("\nNo hay calificaciones válidas para calcular promedio.")
