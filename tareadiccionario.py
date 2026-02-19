# Definir las tareas (usando llaves {})
tareas = {
    "Estudiar Python": False,
    "Comprar leche": False,
    "Hacer ejercicio": True
}

# Mostrar todas las tareas y su estado
print("Lista de tareas:")
for tarea, estado in tareas.items():
    print(tarea, ":", "Completa" if estado else "Incompleta")

print("\n---------------------------------")

# Acceder a un elemento específico
print("Estado de 'Estudiar Python':", tareas.get("Estudiar Python"))

print("\n---------------------------------")

# Marcar una tarea como completada
tareas["Estudiar Python"] = True
print("Se marcó 'Estudiar Python' como completada")

print("\n---------------------------------")

# Mostrar tareas actualizadas
for tarea, estado in tareas.items():
    print(tarea, ":", "Completa" if estado else "Incompleta")

print("\n---------------------------------")

# Eliminar una tarea usando del
del tareas["Comprar leche"]
print(" Se eliminó 'Comprar leche'")

print("\n---------------------------------")

# Usando pop()
valor_eliminado = tareas.pop("Hacer ejercicio")
print("Se eliminó 'Hacer ejercicio' y su estado era:", valor_eliminado)

print("\n---------------------------------")

# Mostrar claves y valores
print("Claves:", tareas.keys())
print("Valores:", tareas.values())

print("\n---------------------------------")

# Agregar nuevas tareas usando update()
nuevas_tareas = {
    "Leer libro": False,
    "Practicar diccionarios": False
}

tareas.update(nuevas_tareas)

print(" Tareas actualizadas con update():")
for tarea, estado in tareas.items():
    print(tarea, ":", "Completa" if estado else "Incompleta")

print("\n---------------------------------")

# Verificación de existencia
print("¿Existe 'Leer libro'?:", "Leer libro" in tareas)
print("¿Existe 'Comprar leche'?:", "Comprar leche" in tareas)

print("\n---------------------------------")

# 1️Copiar diccionario
copia_tareas = tareas.copy()
print("Copia del diccionario:", copia_tareas)

print("\n---------------------------------")

# Diccionario desde función
def obtener_tareas():
    return {
        "Tejer": False,
        "Subir catálogo": True
    }

mas_tareas = obtener_tareas()
print("Tareas desde función:", mas_tareas)
