import json

def cargar_fichero(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def listar_equipos(fichero):
    print("Lista de equipos:")
    for equipo in fichero["equipos"]:
        print(equipo["nombre"], "-", equipo["pais"], "-", equipo["liga"])

def mostrar_numero_jugadores(fichero):
    print("Número de jugadores y goles por equipo:")
    for equipo in fichero["equipos"]:
        total_jugadores = len(equipo["jugadores"])
        total_goles = sum(jugador["goles"] for jugador in equipo["jugadores"])
        print(equipo["nombre"], "-", "Jugadores:", str(total_jugadores), "-", "Goles totales:", str(total_goles))

def mostrar_jugadores_equipo(fichero, nombre_equipo):
    for equipo in fichero["equipos"]:
        if equipo["nombre"] == nombre_equipo:
            print("Jugadores de", nombre_equipo, ":")
            for jugador in equipo["jugadores"]:
                print(jugador["nombre"], "-", jugador["posicion"], "-", "Goles:", str(jugador["goles"]))
            return
    print("Equipo no encontrado")

def buscar_jugador(fichero, nombre_jugador):
    for equipo in fichero["equipos"]:
        for jugador in equipo["jugadores"]:
            if jugador["nombre"] == nombre_jugador:
                print(nombre_jugador, "pertenece a", equipo["nombre"], 
                      "y juega en", equipo["liga"])
                return
    print("Jugador no encontrado")

def buscar_por_goles(fichero, goles_minimos):
    print("Jugadores con", str(goles_minimos), "o más goles:")
    contador = 0
    for equipo in fichero["equipos"]:
        for jugador in equipo["jugadores"]:
            if jugador["goles"] >= goles_minimos:
                print(jugador["nombre"], "-", equipo["nombre"], "-", "Goles:", str(jugador["goles"]))
                contador = contador + 1
    print("Total de jugadores encontrados:", str(contador))

def menu(fichero):
    print("JSON Futbol")
    print(" ")
    print("1. Listar todos los equipos")
    print("2. Mostrar el número de jugadores de un equipo")
    print("3. Pedir equipo y mostrar sus jugadores con su posición y goles")
    print("4. Pedir nombre de jugador y mostrar su equipo y liga")
    print("5. Pedir un mínimo de goles y mostrar los jugadores que han marcado mínimo esa cantidad")
    print("6. Salir")
    print(" ")
    
    opcion = input("Selecciona una opción (1-6): ")
    print(" ")

    if opcion == "1":
        listar_equipos(fichero)
        menu(fichero)
    elif opcion == "2":
        mostrar_numero_jugadores(fichero)
        menu(fichero)
    elif opcion == "3":
        nombre_equipo = input("Introduce el nombre de un equipo: ")
        mostrar_jugadores_equipo(fichero, nombre_equipo)
        menu(fichero)
    elif opcion == "4":
        jugador = input("Introduce el nombre del jugador: ")
        buscar_jugador(fichero, jugador)
        menu(fichero)
    elif opcion == "5":
        goles = int(input("Introduce la cantidad mínima de goles: "))
        buscar_por_goles(fichero, goles)
        menu(fichero)
    elif opcion == "6":
        print("Saliendo del programa...")
        exit()
    else:
        print("Incorrecto, escoja de nuevo")
        menu(fichero)

ruta_archivo = "futbol.json"

try:
    fichero = cargar_fichero(ruta_archivo)
except:
    print("No se encontró el archivo futbol.json en la ruta especificada")
    exit()

menu(fichero)