
try:
    with open("origen.txt", "r", encoding="utf-8") as archivo_origen:
        contenido = archivo_origen.read()

    with open("copia.txt", "w", encoding="utf-8") as archivo_copia:
        archivo_copia.write(contenido)

    print("El contenido se ha copiado exitosamente a 'copia.txt'.")
except FileNotFoundError:
    print("El archivo 'origen.txt' no fue encontrado.")
