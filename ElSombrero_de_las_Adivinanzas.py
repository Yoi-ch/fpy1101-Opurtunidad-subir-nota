from random import randint
import os
import csv

# --- PERSONAJES ---

personajes = []

woody = {"nombre": "Woody", "pelicula": "Toy Story", "pista1": "Tengo una estrella de sheriff en mi pecho", "pista2": "Hay una serpiente en mi bota", "pista3": "Uso sombrero, camisa de cuadros y un chaleco"}
personajes.append(woody)

minion = {"nombre": "Minion", "pelicula": "Mi Villano Favorito", "pista1": "Hablo un idioma que nadie entiende bien", "pista2": "Soy pequeno y amarillo", "pista3": "Tu repela con la papaya!"}
personajes.append(minion)

bob = {"nombre": "Bob Esponja", "pelicula": "Bob Esponja", "pista1": "Vivo en el agua en una casa con forma de fruta", "pista2": "Mi mejor amigo es una estrella de mar", "pista3": "Estan listos chicos? Si capitan estamos listos!"}
personajes.append(bob)

shrek = {"nombre": "Shrek", "pelicula": "Shrek", "pista1": "Vivo solo en un pantano y me gusta asi", "pista2": "Tengo un burro muy hablador como companero", "pista3": "A la vieja muerta me la bajan de la mesa"}
personajes.append(shrek)

rayo = {"nombre": "Rayo McQueen", "pelicula": "Cars", "pista1": "Soy un auto de carreras con un rayo amarillo en los costados", "pista2": "Llevo el numero 95", "pista3": "Ka-chow!"}
personajes.append(rayo)

mike = {"nombre": "Mike Wazowski", "pelicula": "Monsters Inc", "pista1": "Mi trabajo era asustar ninos", "pista2": "Tengo un solo ojo enorme en el centro de mi cara", "pista3": "Quiero convertirme en asustador!"}
personajes.append(mike)

pinocho = {"nombre": "Pinocho", "pelicula": "Pinocho", "pista1": "Soy de madera", "pista2": "Cuando miento una parte de mi cuerpo crece", "pista3": "Fui creado por un anciano carpintero"}
personajes.append(pinocho)

dory = {"nombre": "Dory", "pelicula": "Buscando a Nemo", "pista1": "Hablo el idioma de las ballenas", "pista2": "Tengo una condicion que me impide recordar las cosas", "pista3": "Sufro perdida de memoria a corto plazo"}
personajes.append(dory)

buzz = {"nombre": "Buzz Lightyear", "pelicula": "Toy Story", "pista1": "Creo que soy un guardian espacial del universo", "pista2": "Tengo un traje blanco con botones que hacen sonidos", "pista3": "Al infinito y mas alla!"}
personajes.append(buzz)

remy = {"nombre": "Remy", "pelicula": "Ratatouille", "pista1": "Tengo un talento inusual para alguien de mi especie", "pista2": "Controlo a un humano jalandole el cabello", "pista3": "Sueno con cocinar en los mejores restaurantes"}
personajes.append(remy)

# --- PUNTAJES ---

puntajes = []

# --- FUNCIONES DE MENU ---

def mostrar_menu():
    print("")
    print("========== EL SOMBRERO DE LAS ADIVINANZAS ==========")
    print("1. Jugar")
    print("2. Ver ranking")
    print("3. Salir")
    print("=====================================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion >= 1 and opcion <= 3:
                return opcion
            else:
                print("Opcion invalida. Debe ingresar un numero entre 1 y 3.")
        except ValueError:
            print("Error. Debe ingresar un numero entero.")

# --- FUNCIONES DE VALIDACION ---

def validar_nombre(nombre):
    return nombre.strip() != "" and nombre.replace(" ", "").isalpha()

def validar_continuar(respuesta):
    return respuesta == "s" or respuesta == "n"

# --- FUNCIONES CSV ---

def cargar_puntajes():
    try:
        with open("puntajes.csv", "r", newline="") as archivo:
            lector = csv.reader(archivo)
            next(lector)
            for fila in lector:
                registro = {"nombre": fila[0], "puntaje": int(fila[1])}
                puntajes.append(registro)
    except FileNotFoundError:
        pass

def guardar_puntajes():
    with open("puntajes.csv", "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "puntaje"])
        for p in puntajes:
            escritor.writerow([p["nombre"], p["puntaje"]])

def registrar_puntaje(nombre, puntaje):
    for p in puntajes:
        if p["nombre"].lower() == nombre.lower():
            if puntaje > p["puntaje"]:
                p["puntaje"] = puntaje
            guardar_puntajes()
            return
    registro = {"nombre": nombre, "puntaje": puntaje}
    puntajes.append(registro)
    guardar_puntajes()

def mostrar_ranking():
    if len(puntajes) == 0:
        print("No hay puntajes guardados todavia.")
    else:
        print("--- RANKING ---")
        for p in puntajes:
            print(p["nombre"] + " - " + str(p["puntaje"]) + " puntos")
        print("---------------")

# --- FUNCIONES DEL JUEGO ---

def mostrar_recompensa(puntaje):
    if puntaje >= 800:
        print("RECOMPENSA: Eres el MAESTRO DEL SOMBRERO! Desbloqueaste el modo leyenda!")
    elif puntaje >= 500:
        print("RECOMPENSA: Eres un EXPERTO ANIMADO! Desbloqueaste el rango oro!")
    elif puntaje >= 300:
        print("RECOMPENSA: Eres APRENDIZ DEL SOMBRERO! Sigue practicando!")
    else:
        print("Sigue intentando, puedes mejorar tu puntaje!")

def mostrar_opciones():
    print("========== PERSONAJES ==========")
    print("Woody")
    print("Minion")
    print("Bob Esponja")
    print("Shrek")
    print("Rayo McQueen")
    print("Mike Wazowski")
    print("Pinocho")
    print("Dory")
    print("Buzz Lightyear")
    print("Remy")
    print("================================")

def pedir_respuesta():
    while True:
        try:
            mostrar_opciones()
            respuesta = input("Quien es? (o escribe salir): ")
            respuesta = respuesta.strip()
            if respuesta == "":
                print("Debes escribir algo, intentalo de nuevo.")
            else:
                return respuesta.lower()
        except ValueError:
            print("Error al leer la respuesta, intentalo de nuevo.")

def jugar(nombre_jugador):
    vidas = 3
    puntaje = 0

    print("")
    print("Bienvenido " + nombre_jugador + "!")
    print("Empiezas con 3 vidas.")
    print("Pista 1: 300 puntos, Pista 2: 200 puntos, Pista 3: 100 puntos.")
    print("Si aciertas ganas una vida extra. Si fallas pierdes una vida.")
    print("")

    while vidas > 0:
        indice = randint(0, len(personajes) - 1)
        personaje = personajes[indice]
        acierto = False

        os.system("cls")
        print("El sombrero ha elegido un personaje...")
        print("")

        # Pista 1
        print("Pista 1: " + personaje["pista1"])
        print("Vidas: " + str(vidas) + "  |  Puntaje: " + str(puntaje))
        respuesta = pedir_respuesta()

        if respuesta == "salir":
            print("Puntaje final: " + str(puntaje))
            registrar_puntaje(nombre_jugador, puntaje)
            mostrar_recompensa(puntaje)
            return

        if respuesta == personaje["nombre"].lower():
            puntaje = puntaje + 300
            vidas = vidas + 1
            acierto = True
            print("CORRECTO! Era " + personaje["nombre"] + " de " + personaje["pelicula"])
            print("Ganaste 300 puntos y una vida! Vidas: " + str(vidas))
            print("")
        else:
            vidas = vidas - 1
            print("Incorrecto! Pierdes una vida. Vidas: " + str(vidas))
            print("")

            if vidas == 0:
                print("Sin vidas! El personaje era: " + personaje["nombre"] + " de " + personaje["pelicula"])
                print("Puntaje final: " + str(puntaje))
                registrar_puntaje(nombre_jugador, puntaje)
                mostrar_recompensa(puntaje)
                return

            # Pista 2
            print("Pista 2: " + personaje["pista2"])
            print("Vidas: " + str(vidas) + "  |  Puntaje: " + str(puntaje))
            respuesta = pedir_respuesta()

            if respuesta == "salir":
                print("Puntaje final: " + str(puntaje))
                registrar_puntaje(nombre_jugador, puntaje)
                mostrar_recompensa(puntaje)
                return

            if respuesta == personaje["nombre"].lower():
                puntaje = puntaje + 200
                vidas = vidas + 1
                acierto = True
                print("CORRECTO! Era " + personaje["nombre"] + " de " + personaje["pelicula"])
                print("Ganaste 200 puntos y una vida! Vidas: " + str(vidas))
                print("")
            else:
                vidas = vidas - 1
                print("Incorrecto! Pierdes una vida. Vidas: " + str(vidas))
                print("")

                if vidas == 0:
                    print("Sin vidas! El personaje era: " + personaje["nombre"] + " de " + personaje["pelicula"])
                    print("Puntaje final: " + str(puntaje))
                    registrar_puntaje(nombre_jugador, puntaje)
                    mostrar_recompensa(puntaje)
                    return

                # Pista 3
                print("Pista 3: " + personaje["pista3"])
                print("Vidas: " + str(vidas) + "  |  Puntaje: " + str(puntaje))
                respuesta = pedir_respuesta()

                if respuesta == "salir":
                    print("Puntaje final: " + str(puntaje))
                    registrar_puntaje(nombre_jugador, puntaje)
                    mostrar_recompensa(puntaje)
                    return

                if respuesta == personaje["nombre"].lower():
                    puntaje = puntaje + 100
                    vidas = vidas + 1
                    acierto = True
                    print("CORRECTO! Era " + personaje["nombre"] + " de " + personaje["pelicula"])
                    print("Ganaste 100 puntos y una vida! Vidas: " + str(vidas))
                    print("")
                else:
                    vidas = vidas - 1
                    print("Incorrecto! El personaje era: " + personaje["nombre"] + " de " + personaje["pelicula"])
                    print("")
                    if vidas == 0:
                        print("Sin vidas! Juego terminado.")
                        print("Puntaje final: " + str(puntaje))
                        registrar_puntaje(nombre_jugador, puntaje)
                        mostrar_recompensa(puntaje)
                        return

        if vidas > 0:
            continuar = input("Siguiente personaje? (s/n): ").strip().lower()
            if not validar_continuar(continuar):
                print("Escribe s para si o n para no.")
                continuar = input("Siguiente personaje? (s/n): ").strip().lower()
            if continuar == "n":
                break

    print("")
    print("Puntaje final: " + str(puntaje))
    registrar_puntaje(nombre_jugador, puntaje)
    mostrar_recompensa(puntaje)

# --- PROGRAMA PRINCIPAL ---

def programa_principal():
    cargar_puntajes()

    print("Bienvenido a EL SOMBRERO DE LAS ADIVINANZAS!")
    print("Adivina el personaje animado con las pistas.")
    print("")

    nombre = ""
    while True:
        try:
            nombre = input("Ingresa tu nombre (solo letras): ")
            if validar_nombre(nombre):
                break
            else:
                print("El nombre no puede estar vacio ni tener numeros o simbolos.")
        except ValueError:
            print("Error al leer el nombre, intentalo de nuevo.")

    print("Hola " + nombre + "! Buena suerte!")

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            jugar(nombre)
        elif opcion == 2:
            mostrar_ranking()
        elif opcion == 3:
            print("Hasta luego " + nombre + "! Vuelve pronto.")
            break

programa_principal()