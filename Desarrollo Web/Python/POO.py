# Definición de clases
class Humano():
    mensaje = ""
    def __init__(self, nombre):
        self.nombre = nombre

    def Saludo(self):
        self.mensaje = "Hola, me llamo " + self.nombre
        return self.mensaje


# Crear objeto de clase
Persona = Humano("Alejandro")

# Impresión de objeto
print(type(Persona))

# Impresion de nombre
print(Persona.nombre)

# Utilizacion de métodos
print(Persona.Saludo())

# Clase que hereda de Humano
class Viejo(Humano):
    def __init__(self, nombre):
        Humano.__init__(self, nombre)

    # Sobrecarga de métodos
    def Saludo(self):
        self.mensaje = "Soy un viejo jejeje"
        return self.mensaje

    # Nuevos métodos de clase hijo
    def Despedir(self):
        self.mensaje = "Adios... Estoy cansado :("
        return self.mensaje

    def __str__(self):
        self.mensaje = "Adulto: nombre = " + self.nombre
        return self.mensaje

# Objeto de la clase
Ancestro = Viejo("Rodrigo")
print(Ancestro)  

# Métodos heredados
mensaje = Ancestro.Saludo()
print(mensaje)

# Nuevos métodos
print(Ancestro.Despedir())

print(Ancestro)

