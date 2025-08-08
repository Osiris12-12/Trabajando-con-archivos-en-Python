import csv


with open('estudiantes.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    next(lector) 

    for fila in lector:
        nombre, edad, calificacion = fila
        print(f"{nombre} tiene {edad} años y obtuvo una calificación de {calificacion}")
