def busquedaBinaria(lista, pokemon, inicio, fin):
    if inicio > fin:
        return False

    mitad = (inicio + fin) // 2
    valor_mitad = lista[mitad]

    if valor_mitad == pokemon:
        return True

    if pokemon < valor_mitad:
        return busquedaBinaria(lista, pokemon, inicio, mitad - 1)
    else:
        return busquedaBinaria(lista, pokemon, mitad + 1, fin)    