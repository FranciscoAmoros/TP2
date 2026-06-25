from linkedlist import LinkedList
import hashMap
import hashSet

import json

import os
import keyboard

import random

base_de_datos : hashMap
monedas : hashSet

def precargar():

    global base_de_datos, monedas

    with open("pokedex.json", "r", encoding="utf-8") as archivo:
        pokemones = json.load(archivo)

    for i in range(15):
        done = False
        while not done:

            pokemon = random.choice(pokemones)

            if base_de_datos.buscar(pokemon) == None:

                base_de_datos.agregar(pokemon["id"], pokemon)
                done = True

    for pokemon in pokemones:
        print(pokemon["nombre"], pokemon["tipo"], pokemon["cp"])


equipo = []

PC = LinkedList()

def verEquipo():

    global equipo

    for pokemon in equipo:
        print(pokemon["nombre"], pokemon["tipo"], pokemon["cp"])


def verPokedex():

    os.system("cls")

    with open("pokedex.json", "r", encoding="utf-8") as archivo:
        pokemones = json.load(archivo)


    for pokemon in pokemones:
        print(pokemon["nombre"], pokemon["tipo"], pokemon["cp"])

def main():

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
    print("8. Enviar Pokémon al Centro Pokémon")
    print("9. Transferir Pokémon al Profesor Oak")
    print("10. Deshacer última transferencia")
    print("11. Desafiar Líder de Gimnasio")

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
    if opcion == 2:
        verEquipo()

    print('\nPRESIONE LA TECLA "ESCAPE" PARA VOLVER AL MENÚ.\n')

    return False
        

main()

