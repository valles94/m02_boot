miTexto = "Tres palabras para ti"

# Manera para contar caracteres y cuantas veces ser repiten y meterlos en un dict
frecuencias = {}
for x in miTexto.lower():
    if frecuencias.get(x) == None:
        frecuencias[x] = 1
    else:
        frecuencias[x] += 1
        
print(frecuencias)

# Otra manera de contar caracteres y cuantas veces se repiten y meterlos en un dict
frecuencias_2 = {}
for x in miTexto.lower():
    if x in frecuencias_2:
        frecuencias_2[x] += 1
    else:
        frecuencias_2[x] = 1

print(frecuencias_2)

for x in frecuencias_2.keys():
    print(f"{x} - {frecuencias_2[x]}")
    