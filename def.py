#Es una forma de reutilizar código y de compartimentalizar funciones. 
#También para modular y hacer el ´codigo más claro y funcional
def saludo(nombre, hora):
    if hora <= 12:
        print(f"¡Buenos días, {nombre}!")
    elif hora > 12 and hora < 21:
        print(f"¡Buenas tardes, {nombre}!")
    elif hora >= 21:
        print(f"¡Buenas noches, {nombre}!")
lista_nombres = ["Álvaro", "Claudia", "María", "Laura"]
#for nombre in lista_nombres:
    #saludo(nombre, 11)
dict_nombres = {"estudiante":["Álvaro", "Claudia", "María", "Laura"]}
estudiantes = dict_nombres.values()
for values in estudiantes:
    for nombres in values:
        saludo(nombres, 11)
for nombres in dict_nombres["estudiante"]:
    saludo(nombres, 11)