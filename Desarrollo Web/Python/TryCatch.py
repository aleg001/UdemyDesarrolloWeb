# Implementación de try catch

try:
    texto = open("datos.txt","w")
    texto.write("Datos de archivo")
    texto.close()

except:
    print("Ocurrió un error...")

else:
    print("Manejo de archivos")
    
# Mensaje que se muestra independientemente si el proceso corre o no.
finally:
    print("Finalizado el proceso")