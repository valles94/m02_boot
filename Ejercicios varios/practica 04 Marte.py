cadena = "abcdefghijklmnñopqrstuvwxyz"
contador = ""

for x in cadena:
    ordinal = ord(x)
    ordinal = str(ordinal)
    contador += f"{ordinal} "

print(contador)

contador = contador.split()

conversion = ""
for x in contador:
    caracter = int(x)
    caracter = chr(caracter)
    hexa = int(x)
    valorhexa = hex(hexa)
    conversion += f"{caracter} -- {x} -- {valorhexa}\n"



print(conversion)

diccionario = {}

for x in contador:
    caracter = int(x)
    caracter = chr(caracter)
    hexa = int(x)
    valorhexa = hex(hexa)
    diccionario[caracter] = valorhexa

print(diccionario)


#Conversion de hexadecimal a caracteres
diccionario_rev = {}

for x in diccionario:
    valor = diccionario[x]
    diccionario_rev[valor] = x

print(diccionario_rev)

nuevacadena = "0x68", "0x6f", "0x6c", "0x61"
lista = ""
for x in nuevacadena:
    if x in diccionario_rev.keys():
        valor = diccionario_rev[x]
        lista += valor


print(lista)

