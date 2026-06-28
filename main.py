from linkedlist import LinkedList
import hashMap as hm
import hashSet as hs

from clasePokemon import Pokemon

import profesoroak as profe

from busquedabinaria import busquedaBinaria

import json

import os
import keyboard

import random
import time

import unicodedata

base_de_datos : hm.HashMap
medallas : hs.HashSet

lista_ids_pokedex = []

def precargar():

    global base_de_datos, medallas

    base_de_datos = hm.HashMap(20)
    medallas = hs.HashSet(8)

    with open("pokedex.json", "r", encoding="utf-8") as archivo:
        pokemones = json.load(archivo)

    for i in range(20):
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

    PC.imprimir()

def verEquipo():

    os.system("cls")

    global equipo

    for pokemon in equipo:
        print(pokemon.nombre, pokemon.tipo, pokemon.pc)


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
    print("¡Un Pokemon salvaje apareció!")
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
        dificultad = 0.50
    else:
        dificultad = 0.75

    print("\nTirando la Pokeball", end="", flush=True)

   # time.sleep(1)
    print(" .", end="", flush=True)
    #time.sleep(0.4)
    print(" .", end="", flush=True)
    #time.sleep(0.4)
    print(" .")
    #time.sleep(0.4)

    if random.random() > 0.01:
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

    pokemon = normalizar(input("Ingrese el nombre del Pokémon a buscar: "))

    esta = False

    for p in equipo:
        if normalizar(p.nombre) == pokemon:
            esta = True
            break

    if esta:
        print(f"El Pokémon {pokemon} está en el equipo principal.")
    else:
        print(f"El Pokémon {pokemon} no está en el equipo principal.")

"""

def armarListaIDs():

    lista = []

    for bucket in base_de_datos.buckets:
        for pokemon in bucket:
            lista.append(pokemon[0])

    def quick_sort(lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[len(lista) // 2]

        mayores = []
        iguales = []
        menores = []

        for pokemon in lista:
            if pokemon > pivote:
                mayores.append(pokemon)
            elif pokemon < pivote:
                menores.append(pokemon)
            else:
                iguales.append(pokemon)

        return quick_sort(menores) + iguales + quick_sort(mayores)
    
    lista = quick_sort(lista)

    return lista

def buscarPokemonPokedex():

    global lista_ids_pokedex

    input_valido = False

    while not input_valido:

        try:
            id = int(input("ingrese el id del pokemón que querés buscar: "))
        except ValueError:
            print("solo se pueden ingresar numeros.")
        else:
            input_valido = True
        
    
    resultado = busquedaBinaria(lista_ids_pokedex, id, 0, len(lista_ids_pokedex)-1)

    if not resultado:
        print("no se encontro ese pokemon en la pokédex.")
    else:
        pokemon = base_de_datos.buscar(id)
        print(f"pokemón encontrado: {pokemon.nombre}")
    
"""

def main():

    global lista_ids_pokedex

    precargar()
    profe.main()

    #lista_ids_pokedex = armarListaIDs()

    running = True
    on_menu = True

    on_menu = menu()

    while running:

        if keyboard.is_pressed("escape") and not on_menu:
            on_menu = True
            on_menu = menu()

def menu():

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

    input_valido = False

    while not input_valido:

        try:
            opcion = int(input("\nINGRESE OPCIÓN: \n"))
        except ValueError:
            print("solo se pueden inresar números.")
        else:
            if not 0 < opcion < 12:
                print("opción no válida.")
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
        pass
        #buscarPokemonPokedex()
    elif opcion == 10:
        transferirPokemon()
    elif opcion == 11:
        deshacerTransferencia()

    print('\nPRESIONE LA TECLA "ESCAPE" PARA VOLVER AL MENÚ.\n')

    return False
        

main()


