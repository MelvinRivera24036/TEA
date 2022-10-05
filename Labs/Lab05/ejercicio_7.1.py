try: 
    archivo = input ("Ingrese el nombre del archivo: ")
    f = open (archivo, "r")
    for linea in f:
        print (linea.upper())
except:
    print ("Error, archivo no encontrado")

# print(fhandle.read().upper())