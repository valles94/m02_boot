# Ejercicio zoo
def bucle(entradas, precio, mensaje):
    total = entradas * precio
    if entradas == 1:
        return f"{entradas} entrada de {mensaje} ({precio}€):     {total}€"
    else:
        return f"{entradas} entradas de {mensaje} ({precio}€):     {total}€"
    
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
        edad = input("Ingrese la edad: ")
    return int(edad)


entradas_baby = 0
entradas_menores = 0
entradas_jubilados = 0
entradas_adultos = 0
precio_baby = 0
precio_menores = 14
precio_adultos = 23
precio_jubilados = 18

while True:
    edad = input("Ingrese la edad: ")
    edad = ingrese_edad(edad)
    if edad != 0:
        if edad <= 2:
            entradas_baby += 1
        elif edad > 2 and edad <= 12:
            entradas_menores += 1
        elif edad > 12 and edad < 65:
            entradas_adultos += 1
        elif edad >= 65:
            entradas_jubilados += 1
    elif edad == 0:
        break   
            
total_babys = entradas_baby * precio_baby  
total_menores = entradas_menores * precio_menores
total_adultos = entradas_adultos * precio_adultos
total_jubilados = entradas_jubilados * precio_jubilados
print(bucle(entradas_baby, precio_baby, "baby"))
print(bucle(entradas_menores, precio_menores, "menor"))
print(bucle(entradas_adultos, precio_adultos, "adulto"))
print(bucle(entradas_jubilados, precio_jubilados, "jubilado"))
print(f"- - - - - - - - - - - - - - - - -")
print(f"Total: {total_babys + total_adultos + total_menores + total_jubilados}€")




    




    

