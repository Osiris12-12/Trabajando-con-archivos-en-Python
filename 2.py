
with open('poema.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()


cantidad_lineas = len(lineas)


print(f"El archivo contiene {cantidad_lineas} líneas.")
