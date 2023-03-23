# Ejercicio zoo



def ticket():
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
        edad = int(edad)
        if edad != 0:
            if edad <= 2:
                entradas_baby += 1
            elif edad <= 12:
                entradas_menores += 1
            elif edad > 12 and edad < 65:
                entradas_adultos += 1
            elif edad >= 65:
                entradas_jubilados += 1
        else:
            break
    total_babys = entradas_baby * precio_baby  
    total_menores = entradas_menores * precio_menores
    total_adultos = entradas_adultos * precio_adultos
    total_jubilados = entradas_jubilados * precio_jubilados
    print(f"{entradas_baby} entradas de baby ({precio_baby}€):     {total_babys:8}€")
    print(f"{entradas_menores} entradas de menores ({precio_menores}€):     {total_menores:4}€")
    print(f"{entradas_adultos} entradas de adultos ({precio_adultos}€):     {total_adultos:4}€")
    print(f"{entradas_jubilados} entradas de jubilados ({precio_jubilados}€):     {total_jubilados:2}€")
    print(f"- - - - - - - - - - - - - - - - -")
    print(f"Total: {total_babys + total_adultos + total_menores + total_jubilados}€")

ticket()




    




    

