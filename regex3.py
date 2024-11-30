import re
email = input("Introduzca su correo electrónico: ")
patron_email = "[a-zA-Z0-9_]([\.][a-zA-Z0-9_]+)*@[a-z]+[\.][a-z]{2,3}([\.][a-z]{2,3})*"
matching = re.search(patron_email, email)
if matching:
    print("La dirección de correo es válida.")
else:
    print("La dirección de correo no es válida.")