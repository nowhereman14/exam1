import re
text = input("Introduzca su fecha de nacimiento: ")
patron_date = "(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}"
matching = re.search(patron_date, text)
if matching:
    print("La fecha es válida")
else:
    print("La fecha no es válida")