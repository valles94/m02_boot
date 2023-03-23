# Ejercicio zoo
def bucle(entradas, precio, mensaje):
    total = entradas * precio
    if entradas == 1:
        return f"{entradas} entrada de {mensaje} ({precio}€):\t{total}€"
    else:
        return f"{entradas} entradas de {mensaje} ({precio}€):\t{total}€"
    
def validacion(edad):
    try:
        n = int(edad)
        if n >= 0:
            return True
        else: 
            return False
    except:
        return False
    
def ingrese_edad(edad):
    while not validacion(edad):
        print(f"El valor {edad} no es válido")
        pantalla.locate(1,1)
        edad = input("Ingrese la edad: ")
    return int(edad)


import pantalla

pantalla.clear()
entradas_baby = 0
entradas_menores = 0
entradas_jubilados = 0
entradas_adultos = 0
precio_baby = 0
precio_menores = 14
precio_adultos = 23
precio_jubilados = 18
linea = 3


# MODIFICANDO PARA QUE SE VAYA ACTUALIZANDO EL PRECIO FINAL EN LUGAR DE QUE APAREZCA COMO EN TERCERA VERSION

while True:
    pantalla.locate(1,1)
    edad = input("Ingrese la edad: ")
    edad = ingrese_edad(edad)
    if edad != 0:
        if edad <= 2:
            entradas_baby += 1
            pantalla.locate(3,1)
            print(bucle(entradas_baby, precio_baby, "baby"))
        elif edad > 2 and edad <= 12:
            entradas_menores += 1
            pantalla.locate(4,1)
            print(bucle(entradas_menores, precio_menores, "menor"))
        elif edad > 12 and edad < 65:
            entradas_adultos += 1
            pantalla.locate(5,1)
            print(bucle(entradas_adultos, precio_adultos, "adulto"))
        elif edad >= 65:
            entradas_jubilados += 1
            pantalla.locate(6,1)    
            print(bucle(entradas_jubilados, precio_jubilados, "jubilado"))
    elif edad == 0:
        break   
    total_babys = entradas_baby * precio_baby  
    total_menores = entradas_menores * precio_menores
    total_adultos = entradas_adultos * precio_adultos
    total_jubilados = entradas_jubilados * precio_jubilados    
    pantalla.locate(7,1)
    print(f"Total: {total_babys + total_adultos + total_menores + total_jubilados}€") 

"""total_babys = entradas_baby * precio_baby  
total_menores = entradas_menores * precio_menores
total_adultos = entradas_adultos * precio_adultos
total_jubilados = entradas_jubilados * precio_jubilados
pantalla.locate(7,1)
print()
print(bucle(entradas_baby, precio_baby, "baby"))
print(bucle(entradas_menores, precio_menores, "menor"))
print(bucle(entradas_adultos, precio_adultos, "adulto"))
print(bucle(entradas_jubilados, precio_jubilados, "jubilado"))
print(f"- - - - - - - - - - - - - - - - -")
print(f"Total: {total_babys + total_adultos + total_menores + total_jubilados}€")"""




    




    

