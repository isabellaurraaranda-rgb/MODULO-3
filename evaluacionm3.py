# SISTEMA DE GESTIÓN CLÍNICA
# Evaluación Modular 3


pacientes = []
horas_medicas = []

def registrar_paciente():
    nombre = input("Ingrese nombre del paciente: ")
    rut = input("Ingrese RUT del paciente: ")
    edad = input("Ingrese edad del paciente: ")
    
    paciente = {
        "nombre": nombre,
        "rut": rut,
        "edad": edad
    }
    
    pacientes.append(paciente)
    print("Paciente registrado con éxito.\n")


def agendar_hora():
    if len(pacientes) == 0:
        print("No hay pacientes registrados.\n")
        return
    
    rut = input("Ingrese RUT del paciente: ")
    fecha = input("Ingrese fecha (DD/MM/AAAA): ")
    hora = input("Ingrese hora (HH:MM): ")
    especialidad = input("Ingrese especialidad: ")
    
    hora_medica = {
        "rut": rut,
        "fecha": fecha,
        "hora": hora,
        "especialidad": especialidad
    }
    
    horas_medicas.append(hora_medica)
    print("Hora médica agendada con éxito.\n")


def ver_horas():
    if len(horas_medicas) == 0:
        print("No hay horas agendadas.\n")
    else:
        print("\n--- HORAS MÉDICAS AGENDADAS ---")
        for hora in horas_medicas:
            print(f"RUT: {hora['rut']} - Fecha: {hora['fecha']} - Hora: {hora['hora']} - Especialidad: {hora['especialidad']}")
        print()


def buscar_paciente():
    rut_buscar = input("Ingrese RUT a buscar: ")
    encontrado = False
    
    for paciente in pacientes:
        if paciente["rut"] == rut_buscar:
            print(f"Nombre: {paciente['nombre']}")
            print(f"Edad: {paciente['edad']}\n")
            encontrado = True
            break
    
    if not encontrado:
        print("Paciente no encontrado.\n")


def eliminar_hora():
    rut = input("Ingrese RUT del paciente para eliminar hora: ")
    
    for hora in horas_medicas:
        if hora["rut"] == rut:
            horas_medicas.remove(hora)
            print("Hora eliminada correctamente.\n")
            return
    
    print("No se encontró hora asociada a ese RUT.\n")


def mostrar_menu():
    print("===== SISTEMA CLÍNICA =====")
    print("1. Registrar paciente")
    print("2. Agendar hora médica")
    print("3. Ver horas médicas")
    print("4. Buscar paciente")
    print("5. Eliminar hora médica")
    print("6. Salir")


# Programa principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_paciente()
    elif opcion == "2":
        agendar_hora()
    elif opcion == "3":
        ver_horas()
    elif opcion == "4":
        buscar_paciente()
    elif opcion == "5":
        eliminar_hora()
    elif opcion == "6":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida.\n")