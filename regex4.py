import re
password = "e"
patron_password = "(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[\.#_]).{8,}"
matching = re.search(patron_password, password)
if matching:
    print("La constraseña introducida es válida")
else:
    print("La contraseña introducida no es válida")
lista1 = ["abbbb", "tsjabbds", "kfkedk"]
patron1 = "(?=.*?a[b]+).+"
for element in lista1:
    matching1 = re.search(patron1, element)
    if matching1:
        print("Yes")
    else:
        print("No")