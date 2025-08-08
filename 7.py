
with open('log.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        if 'ERROR' in linea:
            print(linea.strip())  
