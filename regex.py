import re
texto = """¡Hola! ¡Buenas días a todos! Es la clase de la Semana 4.
Las clases empezaron el domingo 06 de febrero de 1999 y el martes 31 de septiembre de 2024.
"""
patron = "el martes \d\d de septiembre de \d\d\d\d"
patron1 = "el [a-z]+ \d{1,2} de [a-z]+ de \d{4}"
patron2 = """el (lunes|martes|miércoles|jueves|viernes|sábado|domingo) (0[1-9]|[12][0-9]|3[01]) de (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre) de (\d{4})"""
print(re.findall(patron2, texto))
matching = re.search(patron2, texto)
print(f"Mi mes favorito es {matching.group(3)}")
