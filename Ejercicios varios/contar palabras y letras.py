cadena = "Esto es una cadena de prueba para contar letras o palabras"

contador = 0
for x in cadena:
    if "e" == x:
        contador += 1

print(contador)

cadena_div = cadena.split()
contador_2 = 0
contador_4 = 0
for x in cadena_div:
    contador_4 += 1

print(contador_4)

for x in cadena_div:
    if "de" == x:
        contador_2 += 1
print(contador_2)

cadena = "Esto es una cadena de prueba para contar letras o palabras"
letras = []
contador_3 = 0

for x in cadena:
    if x not in letras:
        letras.append(x)
    elif x in letras:
        contador_3 += 1
            

       
        
print(len(cadena))
print(len(letras))
print(letras, contador_3)

