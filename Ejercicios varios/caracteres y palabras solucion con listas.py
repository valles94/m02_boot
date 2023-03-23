def existe(letra,lista):
    posicion = 0
    while posicion < len(lista):
        if lista[posicion] == letra:
            return posicion
        posicion += 1
    return None



cadena = "Tres palabras para ti"

palabras = {}
contador = 0
letras = []
frecuencias = []

for x in cadena:
    posicion = existe(x, letras)
    if posicion != None:
        frecuencias[posicion] += 1
    else:
        letras.append(x)
        frecuencias.append(1)
    
indice = 0
while indice < len(letras):
    print(letras[indice], "-", frecuencias[indice])
    indice += 1
    