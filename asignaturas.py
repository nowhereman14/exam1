import json
with open ("asignaturas_grado.json", "r", encoding='utf-8') as json_handler: #json_handler es un objeto gestionador de ficheros
  json_content = json.load(json_handler)
  asignaturas_tercero = []
  for values in json_content["grado"]["Tercero"].values():
    for value in values:
      if value not in asignaturas_tercero:
        asignaturas_tercero.append(value)
print(asignaturas_tercero)