
#Preparacion
def validation_1(p1, p2):
    if len(p1) == len(p2):
        return True

def bucle(palabra, conjunto):
    for x in palabra:
        conjunto.add(x)
    return conjunto

    
def isAnAnagram(p1, p2):
    if validation_1(p1,p2) != True:
        return False
    
    letras_1 = set()
    letras_2 = set()
    bucle(p1, letras_1)
    bucle(p2, letras_2)

    if letras_1 == letras_2:
        return True
    else:
        return False
   
#Entrada
palabra_1 = input("Ingrese palabra 1: ")
palabra_2 = input("Ingrese palabra 2: ")


#Proceso
palabra_1 = palabra_1.lower()
palabra_2 = palabra_2.lower()
consulta = isAnAnagram(palabra_1, palabra_2)

#Salida
if consulta == True:
    print("Es un anagrama")
else:
    print("No es un anagrama")




#   ESTA FUE LA PRIMERA VERSION, LA DE ARRIBA ES LA MEJORADA Y REFACTORIZADA
"""amor = "amor"
roma = "roma"

def validacion(p1, p2):
    if len(p1) == len(p2):
        return True
    else:
        return False

def anagrama(p1, p2):
    if validacion(p1, p2) != True:
        return False        
    listacomparaciones = []
    caracteres_1 = set()
    caracteres_2 = set()
    for caracter1 in p1:
        noAñadasFalse = False
        caracteres_1.add(caracter1)
        for caracter2 in p2: 
            caracteres_2.add(caracter2)   
            if caracter1 == caracter2:
                noAñadasFalse = True
                listacomparaciones.append(True)
        if not noAñadasFalse:
            listacomparaciones.append(False)
    if len(caracteres_1) != len(caracteres_2):
        return False
    if False in listacomparaciones:
        return False
    else:
        return True  

anagrama1 = input("anagrama 1: ")
anagrama2 = input("anagrama 2: ")
if anagrama(anagrama1, anagrama2):
    print("Es un anagrama")
else:
    print("No es un anagrama")"""