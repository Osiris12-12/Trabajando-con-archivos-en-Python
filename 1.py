
nota = input("Escribe una nota para guardar: ")


with open('notas.txt', 'a', encoding='utf-8') as archivo:
    archivo.write(nota + '\n')

print("Nota guardada correctamente.")
