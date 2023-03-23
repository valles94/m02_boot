#Leemos linea por linea del archivo
fEntradas = open("transacciones_2.txt", "r") # llamamos a un archivo externo, la funcion "r" nos permite leer el archivo, no añadir nada

linea = fEntradas.readline() # con la funcion .readkline(), OJO SIN LA "S" DEL FINAL, lo que hacemos es leer solo la linea que queremos del documento

total_entradas = {
    "total_entradas_baby" : 0,
    "total_entradas_menor" : 0,
    "total_entradas_adulto" : 0,
    "total_entradas_jubilado" : 0
}   
# Podriamos importarnos el diccionario ya creado de precios del otro modulo, pero en este caso no nos sirve porque esta con todo el programa, deberia estar en un modulo solo
# from practica_05_Zoo_tercera_version_dict import precios 
precios = {
    "bebe": 0,
    "menor": 14,
    "adulto": 23,
    "jubilado": 18,
}
precios_globales = 0
global_entradas = 0

def impresion(entrada, mensaje, precio):
    total = entrada * precio
    if entrada == 1:
        return f"{entrada} entrada de {mensaje}\t{total}€"
    else:
        return f"{entrada} entradas de {mensaje}\t{total}€"


#       MANERA OPTIMIZADA
while linea != "": #con esta funcion le decimos que mientras la linea sea diferente a "", siga en el bucle, en el momento que no tenga datos, pare
    entradas = linea.split(",")
    total_entradas["total_entradas_baby"] += int(entradas[0])
    global_entradas += int(entradas[0])
    precios_globales += int(entradas[0]) * precios["bebe"]
    total_entradas["total_entradas_menor"] += int(entradas[1])
    global_entradas  += int(entradas[1])
    precios_globales += int(entradas[1]) * precios["menor"]
    total_entradas["total_entradas_adulto"]+= int(entradas[2]) 
    global_entradas  += int(entradas[2]) 
    precios_globales += int(entradas[2]) * precios["adulto"]
    total_entradas["total_entradas_jubilado"] += int(entradas[3])
    global_entradas  += int(entradas[3])
    precios_globales += int(entradas[3]) * precios["jubilado"]
    linea = fEntradas.readline()

print(impresion(total_entradas["total_entradas_baby"],"bebe", precios["bebe"]))
print(impresion(total_entradas["total_entradas_menor"],"menor", precios["menor"]))
print(impresion(total_entradas["total_entradas_adulto"],"adulto", precios["adulto"]))
print(impresion(total_entradas["total_entradas_jubilado"],"jubilado", precios["jubilado"]))
print(f"Total {global_entradas} entradas:\t-\t{precios_globales}€")


# MI MANERA
"""while linea != "": #con esta funcion le decimos que mientras la linea sea diferente a "vacio", siga en el bucle, en el momento que no tenga datos, pare
    linea = linea.split(",")
    if int(linea[0]) != 0:
        total_entradas_baby += int(linea[0])
    elif int(linea[1]) != 0:
        total_entradas_menor += int(linea[1])
    elif int(linea[2]) != 0:
        total_entradas_adulto += int(linea[2])
    elif int(linea[3]) != 0:    
        total_entradas_jubilado += int(linea[3])
    linea = fEntradas.readline()

print(total_entradas_menor)"""