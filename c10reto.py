# ==========================================
# Tuplas en acción: gestión de datos inmutables
# ==========================================

# -----------------------------
# TRAMO 1 – Crear y acceder
# -----------------------------

# 1. Crear tuplas de empleados
empleado1 = ("Ana Torres", "Analista de Datos", 2019)
empleado2 = ("Luis Pérez", "Desarrollador Backend", 2021)
empleado3 = ("María Soto", "Diseñadora UX", 2020)

# Imprimir tuplas completas
print("Empleado 1:", empleado1)
print("Empleado 2:", empleado2)
print("Empleado 3:", empleado3)

# Acceso por índice
print("\nNombre del empleado 1:", empleado1[0])
print("Año de ingreso del empleado 2:", empleado2[-1])

# Intentar modificar (comentado porque genera error)
# empleado1[0] = "Pedro"
# Error: TypeError -> Las tuplas son inmutables


# -----------------------------
# TRAMO 2 – Operaciones
# -----------------------------

# 1. Concatenar tuplas
todos = empleado1 + empleado2 + empleado3
print("\nTupla combinada:", todos)

# 2. Longitud total
print("Cantidad total de elementos:", len(todos))

# 3. Verificar existencia
print("¿Está 'Luis Pérez' en la tupla?", "Luis Pérez" in todos)

# 4. Repetir tupla
print("Tupla repetida:", empleado1 * 2)

# Comprobación de inmutabilidad
print("\nEmpleado1 sigue igual:", empleado1)


# -----------------------------
# TRAMO 3 – Desempaquetado y métodos
# -----------------------------

# 1. Desempaquetado
nombre, cargo, anio = empleado3
print(f"\n{nombre} trabaja como {cargo} desde {anio}.")

# 2. Métodos count() e index()
frutas = ("manzana", "pera", "manzana", "naranja")

print("Veces que aparece 'manzana':", frutas.count("manzana"))
print("Posición de 'naranja':", frutas.index("naranja"))


# -----------------------------
# Resumen final
# -----------------------------
print("\nResumen:")
print("Total de registros individuales:", 3)
print("Total de elementos combinados:", len(todos))
