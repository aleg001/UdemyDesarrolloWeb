# Funciones para decorar

# Funcion para rellenar de astericsos
def rellenarAstericos(Funcion):

    def addAsteriscos():
        print("***************")
        Funcion()
        print("***************")
        Funcion()

    return addAsteriscos

# Funcion para ingreso de cadenas de texto
def Textos():
    texto = input("Ingrese una cadena de texto: ")
    print(texto)

# Se llama a todas las funciones

Textos = rellenarAstericos(Textos)
Textos()