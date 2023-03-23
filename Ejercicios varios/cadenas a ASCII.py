cadena = "Hola mundo"

for x in cadena:
    print(x, "---", ord(x)) #la funcion "ord" te devuelve los valores en ASCII

caracter = int(input("Ingrese un numero del 32 al 127: ")) # la funcion "chr" convierte un numero en caracter en el valor ASCII
print(caracter, "---", chr(caracter))

# convertir cadena de minisculas a mayusculas en valores ASCII

cadena = "Hola mundo"
cadena_2 = "HOLA y hola"

def conversion_mayus(cadena):
    resultado = ""
    for caracter in cadena:
        mayus = ord(caracter)
        espacio = ord(caracter)
        if mayus in range(65, 90):
            resultado += chr(mayus)
        elif espacio == 32:
            resultado += chr(espacio)
        else:
            nuevoCaracter = ord(caracter) - 32
            resultado += chr(nuevoCaracter)
    print(resultado)

def conversion_min(cadena):
    resultado = ""
    for caracter in cadena:
        minus = ord(caracter)
        espacio = ord(caracter)
        if minus in range(97,122):
            resultado += chr(minus)
        elif espacio == 32:
            resultado += chr(espacio)
        else:
            nuevoCaracter = ord(caracter) + 32
            resultado += chr(nuevoCaracter)
    print(resultado)



conversion_mayus(cadena)
conversion_min(cadena_2)
