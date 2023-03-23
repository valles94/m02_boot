#Leemos linea por linea del archivo
fEntradas = open("transacciones_2.txt", "r") # llamamos a un archivo externo, la funcion "r" nos permite leer el archivo, no añadir nada
"""
todas = fEntradas.readlines() # la funcion .readlines() nos permite leer linea tras linea el documento importado
total_entradas_baby = 0
total_entradas_menor = 0
total_entradas_adulto = 0
total_entradas_jubilado = 0


for x in todas:
    print(x)"""



#Leemos el archivo entero

"""todas = fEntradas.read() # con la funcion .read() lo que hacemos es guardar todos los datos en una variable, podemos elegir si queremos leer linea a linea o a lo bestia todo el documento

total_entradas_baby = 0
total_entradas_menor = 0
total_entradas_adulto = 0
total_entradas_jubilado = 0

todas = todas.split("\n")
print(todas)
for x in todas:
    print(x)
"""

# Leemos solo la linea que queremos
linea = fEntradas.readline() # con la funcion .readkline(), OJO SIN LA "S" DEL FINAL, lo que hacemos es leer solo la linea que queremos del documento

total_entradas_baby = 0
total_entradas_menor = 0
total_entradas_adulto = 0
total_entradas_jubilado = 0

print(linea)

while linea != " ": #con esta funcion le decimos que mientras la linea sea diferente a "vacio", siga en el bucle, en el momento que no tenga datos, pare
    print(linea)