aeronaves = []

def mostrar_menu():
    print("SISTEMA DE MANTENIMIENTO AERONAUTICO")
    print("1. Registrar nueva aeronave")
    print("2. Registrar componentes a una aeronave")
    print("3. Registrar horad de vuelo a una aeronave")
    print("4. Consultar reporte de mantenimiento")
    print("5. Realizar mantenimiento a un componente")
    print("6. Mostrar inventario completo")
    print("7. Salir")

def registrar_aeronave():
    print("REGISTRO DE AERONAVE")
    matricula = input("Ingrese la matricula de la aeronave: ").strip().upper()

    for aeronave in aeronaves:
        if aeronave["matricula"] == matricula:
            print("Error: Ya existe una aeronave registrada con esta matricula.")
            return

    modelo = input("Ingrese el modelo de la aeronave: ").strip()

    try:
        horas_iniciales = float(input("Ingrese las horas de vuelo totales acumuladas: "))
    except ValueError:
        print("Error: Debe ingresar un valor numerico para las horas.")
        return

    nueva_aeronave ={
        "matricula": matricula,
        "modelo": modelo,
        "horas_totales": horas_iniciales,
        "componentes": []
    }

    aeronaves.append(nueva_aeronave)
    print(f"Aeronave {matricula} registrada exitosamente con {horas_iniciales} horas totales")

def registrar_componente():
    print("REGISTRO DE COMPONENTE")
    if len(aeronaves) == 0:
        print(" No hay aeronaves registradas. Ingrese una aeronave primero.")
        return

    matricula_busqueda = input("Ingrese a matricula de la aeronave asignada: ").strip().upper()

    aeronave_encontrada = None
    for aeronave in aeronaves:
        if aeronave["matricula"] == matricula_busqueda:
            aeronave_encontrada = aeronave
            break

    if aeronave_encontrada is None:
        print("Error: No se encontro ninguna aeronave con esa matricula.")
        return

    nombre_componente = input("Nombre del componente: ").strip()

    try:
        horas_uso = float(input("Horas de uso desde el ultimo mantenimiento: "))
        limite_horas = float(input("Limite de horas permitidas antes del mantenimiento: "))
    except ValueError:
        print("Error: las horas deben ser valores numericos validos.")
        return

    nuevo_componente = {
        "nombre": nombre_componente,
        "horas_uso": horas_uso,
        "Limite_horas": limite_horas
    }

    aeronave_encontrada["componentes"].append(nuevo_componente)
    print(f"Componente {nombre_componente} agregado a la aeronave {matricula_busqueda}.")

def registrar_vuelo():
    print("REGISTRO DE HORAS DE VUELO")
    if len(aeronaves) == 0:
        print("No hay aeronaves registradas.")
        return

    matricula_busqueda = input("Ingrese la matricula de la aeronave que volo: ").strip().upper()

    aeronave_encontrada = None
    for aeronave in aeronaves:
        if aeronave["matricula"] == matricula_busqueda:
            aeronave_encontrada = aeronave 
            break

    if aeronave_encontrada is None:
        print("Error: No se encontro la aeronave buscada.")
        return

    try:
        horas_voladas = float(input("Ingrese la cantidad de horas voladas en este trayecto: "))
        if horas_voladas <= 0:
            print("Error: las horas de vuelo deben ser un numero positivo.")
            return
    except ValueError:
        print("Error: Ingrese un valor numerico valido.")
        return

    aeronave_encontrada["horas_totales"] += horas_voladas
    for comp in aeronave_encontrada["componentes"]:
        comp["Horas_uso"] += horas_voladas

    print(f"Se han sumado {horas_voladas} horas de vuelo a la aeronave {matricula_busqueda}.")
    print(f" Nuevas horas totales acumuladas de la aeronave: {aeronave_encontrada['horas_totales']} horas.")

def consultar_mantenimiento():
    print("CONSULTA DE MANTENIMIENTO")
    if len(aeronaves) == 0:
        print("No hay aeronaves registradas en el sistema.")
        return

    hay_alertas = False

    for aeronave in aeronaves:
        matricula = aeronave["matricula"]
        modelo = aeronave["modelo"]
        horas_totales = aeronave["horas_totales"]
        lista_componentes = aeronave["componentes"]

        for comp in lista_componentes:
            if comp["horas_uso"] >= comp["limite_horas"]:
                hay_alertas = True
                exceso = comp["horas_uso"] - comp["limite_horas"]
            print(f"ALERTA MANTENIMIENTO, Aeronave: {matricula} ({modelo})")
            print(f" Horas Totales Acumuladas de la Aeronave: {horas_totales} horas")
            print(f" Componente afectado: {comp['nombre']}")
            print(f" Horas de uso desde el ultimo mantenimiento: {comp['horas_uso']} horas")
            print(F" Limite maximo de mantenimiento: {comp['limite_horas']} horas")
            print(f" Estadp: Excedido por {exceso:.2f} horas. REQUIERE MANTENIMIENTO INMEDIATO.")
            print("ALERTA" * 5)

        if not hay_alertas:
            print("Todos los componentes estan dentro del margen operativo seguro.")

def realizar_mantenimiento():
    print("REGISTRAR MANTENIMIENTO REALIZADO")
    if len(aeronaves) == 0:
        print("No hay aeronaves registradas en el sistema.")
        return

    matricula_busqueda = input("Ingrese la matricula de la aeronave: ").strip().upper()

    aeronave_encontrada = None
    for aeronave in aeronaves:
        if aeronave["matricula"] == matricula_busqueda:
            aeronave_encontrada = aeronave 
            break
    if aeronave_encontrada is None:
        print("Error: No se encontro la aeronave especificada.")
        return

    if len(aeronave_encontrada["componentes"]) == 0:
        print("La aeronave no tiene componentes registrados.")
        return

    nombre_comp = input("Ingrese el nombre del componente al que se le hizo mantenimiento: ").strip()

    componente_encontrado = None
    for comp in aeronave_encontrada["componentes"]:
        if comp["nombre"].lower() == nombre_comp.lower():
            componente_encontrado = comp
            break
    if componente_encontrado is None:
        print("Error: Componente no encontrado en est aeronave.")
        return
    componente_encontrado["horas_uso"] = 0.0

    print(f"Mantenimiento realizado con exito en el componente: {componente_encontrado['nombre']}.")
    print("Horas desde ultimo mantenimiento reiniciadas a : 0.0 horas.")
    print(f"Horas totales acumuladas de la aeronave se mantienen en: {aeronave_encontrada['horas_totales']} horas.")

def mostrar_inventario():
    print("INVENTARIO GENERAL")
    if len(aeronaves) == 0:
        print("No hay datos registrados.")
        return
    
    for aeronave in aeronaves:
        print(f"Aeronave: {aeronave['matricula']} Modelo: {aeronave['modelo']}")
        print(f"HORAS TOTALES DE VUELO: {aeronave['horas_totales']} horas")

        if len(aeronave["componentes"]) == 0:
            print("SIn componentes registrados")
        else:
            for comp in aeronave["componentes"]:
                print(f"Componente: {comp['nombre']}")
                print(f"Horas tras ultimo mantenimiento: {comp['horas_uso']} horas  /  {comp['limite_horas']} horas max")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-7): ").strip()

        if opcion == "1":
            registrar_aeronave()
        elif opcion == "2":
            registrar_componente()
        elif opcion == "3":
            registrar_vuelo()
        elif opcion == "4":
            consultar_mantenimiento()
        elif opcion == "5":
            realizar_mantenimiento()
        elif opcion == "6":
            mostrar_inventario()
        elif opcion == "7":
            print("Cerrando sistema")
            break
        else:
            print("Opcion no valida. Elija un numero entre 1 y 7.")

if __name__ == "__main__":
    main()