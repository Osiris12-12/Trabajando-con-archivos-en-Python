
suma_total = 0


with open("datos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        numero = int(linea.strip())  
        suma_total += numero


print(f"La suma total de los números es: {suma_total}")
