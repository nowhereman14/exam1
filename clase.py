import json
with open ("clase.json", "r", encoding='utf-8') as json_handler:
  json_content = json.load(json_handler)
  list_dicc = json_content["clase"]
  i = 0
  while i < len(list_dicc):
    if list_dicc[i]["rol"] == "Profe":
     print(f'La profesora es {list_dicc[i]["name"]}')
    elif list_dicc[i]["rol"] == "alumno":
      print(f'{list_dicc[i]["name"]} es un alumno')
    elif list_dicc[i]["rol"] == "alumna":
      print(f'{list_dicc[i]["name"]} es una alumna')
    i += 1