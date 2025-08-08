
numeros = [10, 20, 30, 40, 50]


with open("numeros.txt", "w", encoding="utf-8") as archivo:
    for numero in numeros:
        archivo.write(str(numero) + "\n")

print("Los números se han escrito correctamente en 'numeros.txt'.")
