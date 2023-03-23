# Ejercicio zoo
def bucle(entradas, precio, mensaje):
    total = entradas * precio
    if entradas == 1:
        return f"{entradas} entrada de {mensaje} ({precio}€): \t{float(total)}€"
    else:
        return f"{entradas} entradas de {mensaje} ({precio}€):\t{float(total)}€"
    
def validacion(edad):
    try:
        n = int(edad)
        if n >= 0:
            return True
        else: 
            return False
    except:
        return False
    
def ingrese_edad():
    pantalla.locate(1,1)
    pantalla.clearLine()
    edad = input("Ingrese la edad: ")
    while not validacion(edad):
        pantalla.locate(15,1)
        pantalla.format(1,31,41)
        print(f"El valor {edad} no es válido", end = " ")
        pantalla.reset()
        pantalla.locate(1,1)
        pantalla.clearLine()
        edad = input("Ingrese la edad: ")
        pantalla.clearLine(15,1)
    return int(edad)

import pantalla

entradas = {
    "entradas_baby" : 0,
    "entradas_menores" : 0,
    "entradas_jubilados" : 0,
    "entradas_adultos" : 0    
}
precios = {
    "precio_baby" : 00,
    "precio_menores" : 14,
    "precio_adultos" : 23,
    "precio_jubilados" : 18
}
pantalla.clear()

while True:
    edad = ingrese_edad()
    if edad != 0:
        if edad <= 2:
            entradas["entradas_baby"] += 1
            pantalla.locate(4,1)
            print(bucle(entradas["entradas_baby"], precios["precio_baby"], "baby"))
        elif edad > 2 and edad <= 12:
            entradas["entradas_menores"] += 1
            pantalla.locate(5,1)
            print(bucle(entradas["entradas_menores"], precios['precio_menores'], "menor"))
        elif edad > 12 and edad < 65:
            entradas["entradas_adultos"] += 1
            pantalla.locate(6,1)
            print(bucle(entradas['entradas_adultos'], precios['precio_adultos'], "adulto"))
        elif edad >= 65:
            entradas["entradas_jubilados"] += 1
            pantalla.locate(7,1)    
            print(bucle(entradas['entradas_jubilados'], precios['precio_jubilados'], "jubilado"))
    elif edad == 0:
        break  
    total_babys = entradas["entradas_baby"] * precios["precio_baby"]  
    total_menores = entradas["entradas_menores"] * precios['precio_menores']
    total_adultos = entradas['entradas_adultos'] * precios['precio_adultos']
    total_jubilados = entradas['entradas_jubilados'] * precios['precio_jubilados']
    pantalla.locate(8,1)
    print()  
    print(f"- - - - - - - - - - - - - - - - -")
    pantalla.bold()
    print(f"Total: {float(total_babys + total_adultos + total_menores + total_jubilados)}€\n")
    pantalla.regular()

fEntradas = open("transacciones_2.txt", "a+") # con esta funcion le decimos que abra el fichero llamado "transacciones," la "a" es un comando que permite añadir cada dato al anterior, es un append, y añadir datos y el "+" dice que si no existe ese fichero lo cree, si el fichero existiese no haria falta poner el +
transaccion = f"{entradas['entradas_baby']},{entradas['entradas_menores']},{entradas['entradas_adultos']},{entradas['entradas_jubilados']}\n"
fEntradas.write(transaccion)
fEntradas.close()
pantalla.locate(11,1)
print() 



