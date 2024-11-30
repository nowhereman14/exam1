def contador(texto):
    i = 0
    while i < len(texto):
        i += 1
    #print(f"La longitud del texto en caracteres es: {i}")
    texto = texto.split(" ")
    a = 0
    while a < len(texto):
        a += 1
    #print(f"La longitud del texto en palabras es: {a}")
    return(a, i)
texto = "Por ejemplo, si queremos obtener los datos de cada uno de los empleados de administración junto con los datos del despacho donde trabajan pero sin repetir valores de atributos superfluos, haremos la siguiente combinación natural, que requiere una redenominación previa."
texto_2 = """Como hemos comentado en anteriores comunicaciones, estamos organizando un concierto en el que el cartel estará compuesto íntegramente por proyectos residentes en Metrónomo.
El concierto tendrá lugar el próximo martes 3 de diciembre a las 19:00 en el Centro Cultural Pilar Miró.
En esta edición contaremos con la participación de Bob Ol-Ombs, Candace, Flaco Rodríguez, Situasound y Suko Pyramid.
La duración total del evento será de 2 horas. La entrada es gratuita y puede recogerse en el Centro Cultural Pilar Miró desde 2 horas antes del comienzo de los conciertos.
Os animamos a aprovechar esta ocasión de disfrutar de la música en directo y a apoyar a vuestros compañeros. ¡Nos vemos el día 3!"""
#texto_3 = input("Introduzca una oración: ")
l = contador(texto_2)
print(l)