
try:
    with open("frases.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()  
        palabras = contenido.split()  
        cantidad_palabras = len(palabras)  

    print("Cantidad total de palabras en el archivo:", cantidad_palabras)
except FileNotFoundError:
    print("El archivo 'frases.txt' no fue encontrado.")
