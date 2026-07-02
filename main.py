from linkedlist import LinkedList
import hashMap as hm
import hashSet as hs

from clasePokemon import Pokemon

import profesoroak as profe
import centropokemon

from busquedabinaria import busquedaBinaria

import json

import os
import keyboard

import random
import time

import unicodedata

base_de_datos : hm.HashMap
medallas : hs.HashSet

running = True

def precargar():

    global base_de_datos, medallas

    base_de_datos = hm.HashMap(59)
    medallas = hs.HashSet(8)

    with open("pokedex.json", "r", encoding="utf-8") as archivo:
        pokemones = json.load(archivo)

    for i in range(59):
        done = False
        while not done:

            pokemon = random.choice(pokemones)

            if base_de_datos.buscar(pokemon["id"]) == None:

                instancia_pokemon = Pokemon(pokemon["id"], pokemon["nombre"], pokemon["tipo"], pokemon["cp"])

                base_de_datos.agregar(pokemon["id"], instancia_pokemon)
                done = True

    with open("medallas.json", "r", encoding="utf-8") as archivo:
        medallas_json = json.load(archivo)

    for i in range(2):
        done = False
        while not done:

            medalla = random.choice(medallas_json)

            if not medallas.buscar(medalla["id"]):

                medallas.agregar(medalla["id"])
                done = True


equipo = []

PC = LinkedList()

def verPC():

    os.system("cls")

    if PC.size() == 0:
        print("no tenes ningún pokemón en la PC.")
        return

    PC.imprimir()

def verEquipo():

    os.system("cls")

    global equipo

    if not equipo:
        print("no tenes ningún pokemón en el equipo.")
        return

    for indice, pokemon in enumerate(equipo):
        print(f"{indice+1}. {pokemon.nombre} | {pokemon.tipo} | {pokemon.pc}")


def verPokedex():

    os.system("cls")

    base_de_datos.mostrar()


def verMedallas():

    os.system("cls")

    medallas.mostrar()

def transferirPokemon():
    
    os.system("cls")

    global equipo, PC

    if PC.is_empty():
        print("No hay Pokémon en la PC para transferir.")
        return

    print("elija el pokémon que desea transferir al Profesor Oak (ingrese el número correspondiente):")
    PC.imprimir()

    try:
        opcion = int(input("\nINGRESE OPCIÓN: \n"))
    except ValueError:
        print("solo se pueden inresar números.")
    else:
        if opcion <= 0 or opcion > PC.size():
            print("opción no válida.")
        else:
            elemento_actual = PC.head
            for i in range(opcion-1):
                elemento_actual = elemento_actual.next

            pokemon_a_transferir = elemento_actual.data

            PC.delete(pokemon_a_transferir)
            profe.transferir(pokemon_a_transferir)

            print(f"{pokemon_a_transferir.nombre} ha sido transferido al Profesor Oak.")

def deshacerTransferencia():
    
    os.system("cls")

    global equipo, PC

    pokemon_recuperado = profe.deshacerTransferencia()

    if pokemon_recuperado == "Stack is empty":
        print("No hay transferencias para deshacer.")
    else:
        PC.insert(pokemon_recuperado, 0)
        print(f"{pokemon_recuperado.nombre} ha sido recuperado del Profesor Oak y agregado a la pc.")

def capturarPokemon():
    
    os.system("cls")

    global equipo, PC

    print()
    print("¡Un Pokemón salvaje apareció!")
    print()

    salvaje = base_de_datos.obtenerPokemonRandom()[1]

    print(f"  ¡Es un {salvaje.nombre}! ({salvaje.tipo}) | PC: {salvaje.pc}")
    print()

    intentar = input("¿Querés intentar atraparlo? (s/n): ").strip().lower()

    if intentar != "s":
        print("\nDejaste escapar al Pokemon...")
        return
    
    ids_equipo = []

    for pokemon_equipo in equipo:
        ids_equipo.append(pokemon_equipo.id)


    ids_pc = PC.obtener_ids()


    if salvaje.id in ids_equipo or salvaje.id in ids_pc:
        print(f"\nYa tenés un {salvaje.nombre} en tu equipo o PC.")
        return

    
    if salvaje.pc < 300:
        dificultad = 0.20
    elif salvaje.pc < 550:
        dificultad = 0.45
    else:
        dificultad = 0.60

    print("\nTirando la Pokeball", end="", flush=True)

    """
    time.sleep(1)
    print(" .", end="", flush=True)
    time.sleep(0.4)
    print(" .", end="", flush=True)
    time.sleep(0.4)
    print(" .")
    time.sleep(0.4)
    """

    if random.random() > 0.01:#dificultad:
        nuevo = Pokemon(salvaje.id, salvaje.nombre, salvaje.tipo, salvaje.pc)
        if len(equipo) < 6:
            equipo.append(nuevo)
            print(f"\n¡Atrapaste a {nuevo.nombre}! Fue añadido al equipo ({len(equipo)}/6)")
        else:
            PC.append(nuevo)
            print(f"\n¡Atrapaste a {nuevo.nombre}! Equipo lleno, fue enviado a la PC")
    else:
        print(f"\n¡{salvaje.nombre} escapó! Más suerte la próxima.")


def ordenarPc():

    os.system("cls")

    print("¿Cómo querés ordenar tu PC?\n")

    print("1. Ordenamiento Alfabético")
    print("2. Ordenamiento por Tipo")
    print("3. Ordenamiento Competitivo")
    print("4. Salir")

    opcion_valida = False

    while not opcion_valida:

        try:
            respuesta = int(input("\nRespuesta: "))
        except ValueError:
            print("solo se pueden ingresar numeros")
        else:
            if respuesta < 1 or respuesta > 4:
                print("opción no válida")
            else:
                opcion_valida = True

            
    if respuesta == 1:
        PC.ordenar_por_nombre()
    elif respuesta == 2:
        PC.ordenar_por_tipo()
    elif respuesta == 3:
        PC.ordenar_por_poder_combate()
    elif respuesta == 4:
        return
    

def normalizar(texto):
    texto = texto.lower().strip()      
    texto = "".join(texto.split())     
    texto = "".join(
        c for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    )                             
    return texto


def buscarPokemonEquipo():

    os.system("cls")

    pokemon_ingresado = normalizar(input("Ingrese el nombre del Pokémon a buscar: "))

    esta = False


    for p in equipo:
        if normalizar(p.nombre) == pokemon_ingresado:
            esta = True
            pokemon = p
            break

    if esta:
        print(f"Pokemón encontrado en el equipo: {pokemon.nombre} | {pokemon.tipo} | {pokemon.pc}")
    else:
        print(f"El Pokémon {pokemon_ingresado} no está en el equipo principal.")



def buscarPokemonPokedex():

    os.system("cls")

    global lista_ids_pokedex

    input_valido = False

    while not input_valido:

        try:
            id = int(input("ingrese el id del pokemón que querés buscar: "))
        except ValueError:
            print("solo se pueden ingresar numeros.")
        else:
            input_valido = True
        
    
    pokemon = base_de_datos.buscar(id)

    if not pokemon:
        print("no se encontro ese pokemon en la pokédex.")
    else:
        print(f"pokemón encontrado: {pokemon.nombre} | {pokemon.tipo} | {pokemon.pc}")
    


def desafiarLider():

    global equipo, base_de_datos, medallas

    os.system("cls")

    if not len(equipo) == 6:
        print(f"no se puede pelear porque no tenes el equipo completo ({len(equipo)}/6)")
        return

    print("1. Roca")
    print("2. Cascada")
    print("3. Trueno")
    print("4. Arcoiris")
    print("5. Alma")
    print("6. Pantano")
    print("7. Volcan")
    print("8. Tierra")

    opciones = {
        1: "Roca",
        2: "Cascada",
        3: "Trueno",
        4: "Arcoíris",
        5: "Alma",
        6: "Pantano",
        7: "Volcán",
        8: "Tierra"
    
    }

    dificultades = {
        1: 300,
        2: 350,
        3: 400,
        4: 450,
        5: 500,
        6: 550,
        7: 600,
        8: 650
    }

    input_valido = False

    while not input_valido:
        try:
            opcion = int(input("\ningrese opcion: "))

        except ValueError:
            print("solo se pueden ingresar numeros")
        else:
            if opcion < 1 or opcion > 8:
                print("opcion no valida")
            else:
                input_valido = True

    if medallas.buscar(opcion):

        print("ya tienes esa medalla.")

    else:


        dificultad = dificultades[opcion]

        os.system("cls")
        print(f"PELEA CONTRA LIDER DE GIMNASIO DE {opciones[opcion].upper()}")


        lider = []


        while len(lider) < 6:


            pokemon = base_de_datos.obtenerPokemonRandom()[1]


            if abs(pokemon.pc - dificultad) <= 50 and pokemon not in lider:
                lider.append(pokemon)


        ronda = 1
        equipo_copia = equipo.copy()

        rondas_jugador = 0
        rondas_lider = 0

        nombre_medalla = opciones[opcion].upper()
        indice_medalla = opcion


        while not ronda == 6:

            os.system("cls")
            print(f"PELEA CONTRA LIDER DE GIMNASIO DE {nombre_medalla}")
            print(f"RONDA {ronda}")
            print("")

            print("ELEGIR POKEMON")

            for indice, p in enumerate(equipo_copia, start=1):
                print(f"{indice}. {p.nombre} - {p.pc}")

            input_valido = False

            while not input_valido:
                try:
                    opcion = int(input("\ningrese opcion: "))

                except ValueError:
                    print("solo se pueden ingresar numeros")
                else:
                    if opcion < 1 or opcion > len(equipo_copia):
                        print("opcion no valida")
                    else:
                        input_valido = True

            pokemon_jugador = equipo_copia[opcion-1]
            pokemon_lider = random.choice(lider)

            print("\n")
            print(f"POKEMON DEL JUGADOR: {pokemon_jugador.nombre} - {pokemon_jugador.pc}")
            print(f"POKEMON DEL LIDER: {pokemon_lider.nombre} - {pokemon_lider.pc}")

            print("\nProcesadondo pelea", end="", flush=True)

            time.sleep(1)
            print(" .", end="", flush=True)
            time.sleep(0.4)
            print(" .", end="", flush=True)
            time.sleep(0.4)
            print(" .")
            time.sleep(3)

            poder_jugador = pokemon_jugador.pc + random.randint(-50, 50)
            poder_lider = pokemon_lider.pc + random.randint(-50, 50)

            if poder_jugador >= poder_lider:
                print(f"Ganó el jugador la ronda {ronda}")
                lider.remove(pokemon_lider)
                daño = (pokemon_lider.pc) / 10
                pokemon_jugador.pc -= daño # desgaste
                print("pokemón del líder eliminado")
                print(f"pokemón del jugador - {daño} de pc")
                rondas_jugador += 1
            else:
                print(f"Ganó el líder la ronda {ronda}")
                equipo_copia.remove(pokemon_jugador)
                daño = (pokemon_jugador.pc) / 10
                pokemon_lider.pc -=  daño # desgaste
                print("pokemón del jugador eliminado")
                print(f"pokemón del líder - {daño} de pc")
                rondas_lider += 1

            time.sleep(2)

            ronda += 1

        os.system("cls")
        print("BATALLA TERMINADA")
        if rondas_jugador > rondas_lider:
            print("el jugador ganó la batalla.")
            print(f"medalla de {nombre_medalla} obtenida.")
            medallas.agregar(indice_medalla)
        else:
            print("el líder ganó la batalla.")


def armarEquipo():

    if PC.size() == 0:
        os.system("cls")
        print("No hay pokemones suficientes para cambiar.")
        return

    equipo_nuevo = []
    indices_usados = []
    mensaje = ""

    while len(equipo_nuevo) < 6:

        os.system("cls")

        print("----- POKEMONES DE LA PC -----\n")
        for indice in range(PC.size()):
            p = PC.find_by_index(indice)
            print(f"{indice} | {p.nombre} | {p.tipo} | {p.pc}")

        print("\n----- POKEMONES DEL EQUIPO ACTUAL -----\n")
        for indice, pokemon in enumerate(equipo):
            print(f"{PC.size()+indice} | {pokemon.nombre} | {pokemon.tipo} | {pokemon.pc}")

        if equipo_nuevo:
            print("\n----- YA ELEGISTE -----\n")
            for pokemon in equipo_nuevo:
                print(f"- {pokemon.nombre} | {pokemon.tipo} | {pokemon.pc}")

        if mensaje:
            print(f"\n{mensaje}")

        total_disponibles = PC.size() + len(equipo)

        try:
            indice = int(input(f"\nElegí el pokémon #{len(equipo_nuevo)+1} para tu equipo (índice): "))
        except ValueError:
            mensaje = "Ingresá un número válido."
            continue

        if indice < 0 or indice >= total_disponibles:
            mensaje = "Ese índice no existe. Intentá de nuevo."
            continue

        if indice in indices_usados:
            mensaje = "Ese pokémon ya fue elegido. Elegí otro."
            continue

        if indice < PC.size():
            pokemon_elegido = PC.find_by_index(indice)
        else:
            pokemon_elegido = equipo[indice - PC.size()]

        equipo_nuevo.append(pokemon_elegido)
        indices_usados.append(indice)
        mensaje = f"{pokemon_elegido.nombre} agregado al equipo nuevo."

    for pokemon in equipo:
        if pokemon not in equipo_nuevo:
            PC.append(pokemon)

    for pokemon in equipo_nuevo:
        if pokemon not in equipo:
            PC.delete(pokemon)

    equipo[:] = equipo_nuevo

    os.system("cls")
    print("¡Equipo armado con éxito!\n")
    for pokemon in equipo:
        print(f"- {pokemon.nombre} | {pokemon.tipo} | {pokemon.pc}")


def salir():

    global running

    os.system("cls")
    print("Hasta pronto!")
    running = False
    exit()

def main():

    global running

    precargar()
    profe.main()
    centropokemon.main(base_de_datos)
    

    running = True
    on_menu = True

    on_menu = menu()

    while running:

        if keyboard.is_pressed("escape") and not on_menu:
            on_menu = True
            on_menu = menu()


def enviarPokemonCentro():

    global equipo

    centropokemon.curar(equipo)


def mostrar_opciones():

    os.system("cls")

    print("1. Ver Pokédex")
    print("2. Ver Equipo Principal")
    print("3. Ver PC")
    print("4. Ver Medallas")
    print("5. Capturar nuevo Pokémon")
    print("6. Ordenar PC")
    print("7. Buscar Pokémon en Equipo")
    print("8. Buscar Pokémon en Pokédex")
    print("9. Enviar Pokémon al Centro Pokémon")
    print("10. Transferir Pokémon al Profesor Oak")
    print("11. Deshacer última transferencia")
    print("12. Desafiar Líder de Gimnasio")
    print("13. Armar equipo")
    print("14. Salir")

def menu():

    input_valido = False

    while not input_valido:

        mostrar_opciones()

        try:
            opcion = int(input("\nINGRESE OPCIÓN: \n"))
        except ValueError:
            continue
        else:

            if not 0 < opcion < 15:
                continue
            else:
                input_valido = True

    if opcion == 1:
        verPokedex()
    elif opcion == 2:
        verEquipo()
    elif opcion == 3:
        verPC()
    elif opcion == 4:
        verMedallas()
    elif opcion == 5:
        capturarPokemon()
    elif opcion == 6:
        ordenarPc()
    elif opcion == 7:
        buscarPokemonEquipo()
    elif opcion == 8:
        buscarPokemonPokedex()
    elif opcion == 9:
        enviarPokemonCentro()
    elif opcion == 10:
        transferirPokemon()
    elif opcion == 11:
        deshacerTransferencia()
    elif opcion == 12:
        desafiarLider()
    elif opcion == 13:
        armarEquipo()
    elif opcion == 14:
        salir()

    print('\nPRESIONE LA TECLA "ESCAPE" PARA VOLVER AL MENÚ.\n')

    return False
        

main()


