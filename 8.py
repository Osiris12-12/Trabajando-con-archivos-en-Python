
try:
    with open("nombres.txt", "r", encoding="utf-8") as archivo:

        for linea in archivo:
            nombre = linea.strip() 
            print(nombre)
except FileNotFoundError:
    print("El archivo 'nombres.txt' no fue encontrado.")
