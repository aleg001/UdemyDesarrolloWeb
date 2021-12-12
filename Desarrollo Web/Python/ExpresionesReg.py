# Expresiones re


# Se importa el módulo re
import re

# String original
informacion = "El piano es de 88 teclas. Este piano es de la marca Steinway and Sons."

# String a buscar
pattern = input("\nIngrese la palabra a buscar: ")

# Busqueda de similitudes
findSimilar = re.search(pattern, informacion)

# Verificacion de similitudes
if findSimilar:
    print("\nSe ha encontrado la similitud con {}".format(pattern))

    # Se cuenta la cantidad de veces que aparece en el string.
    cantidadVeces = re.findall(pattern, informacion)
    cantVeces = len(cantidadVeces)

    # Se busca la posicion inicial dentro de texto
    posInicial = findSimilar.start()

    # Se busca posicion final dentro de texto
    posFinal = findSimilar.end()
    #print("Empieza en {} y termina en {}".format(posInicial, posFinal))

    # Se muestra cantidad de veces
    print("Se encontró",cantVeces,"veces la palabra "+ pattern)
else:
    print("El texto no encontró coincidencias")
