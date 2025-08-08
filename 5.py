import json


persona = {
    'nombre': 'Carlos',
    'edad': 28,
    'ciudad': 'Santo Domingo'
}


with open('persona.json', 'w', encoding='utf-8') as archivo:
    json.dump(persona, archivo, ensure_ascii=False, indent=4)
