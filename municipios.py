import json
with open ("municipios-es.json", "r", encoding="utf-8") as json_handler:
    json_content = json.load(json_handler)
    print(json_content.keys())
    print(json_content["meta"].keys())
    print(type(json_content["data"]))
    print(type(json_content["meta"]["view"]))
    print(len(json_content["data"]))
    print(json_content["data"][0])
    print(len(json_content["data"][0]))
    print(json_content["data"][0][-2])
    lista_municipios = json_content["data"]
    i = 0
    while i < len(lista_municipios):
        print(lista_municipios[i][-2])
        i+=1
    for municipios in lista_municipios:
        print(municipios[0])