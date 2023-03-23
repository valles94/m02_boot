

def devuelveSuma(a, b):
    suma = a + b
    return suma

def devuelveResta(numero1, numero2):
    resta = numero1 - numero2
    return resta

def devuelveMultiplicacion(numero1, numero2):
    multiplicar = numero1 * numero2
    return multiplicar

def devuelveDivision(numero1, numero2):
    dividir = numero1 / numero2
    return dividir

def bucle(x):
    calculando = True
    while calculando:
        if x.isdigit():
            x = int(x)
            break
        elif x[0] == "-" and x[1].isdigit():
            x = int(x)
            break
        else:
            print("Valor no válido")
            x = input("Ingrese un numero: ")
    return x

def calcular():
    numero1 = input("Ingrese un numero: ")
    numero1 = bucle(numero1)
    numero2 = input("Ingrese otro numero: ")
    numero2 = bucle(numero2)

    numero1 = int(numero1) / 10 
    numero2 = int(numero2) / 10  
    print(f"{numero1} + {numero2} = {devuelveSuma(numero1, numero2):.1f}")
    print(f"{numero1} - {numero2} = {devuelveResta(numero1, numero2):.1f}")
    print(f"{numero1} * {numero2} = {devuelveMultiplicacion(numero1, numero2):.1f}")
    print(f"{numero1} / {numero2} = {devuelveDivision(numero1, numero2):.2f}")

calcular()





"""def calcular():
    calculando = True
    calculando2 = True
    numero1 = input("Ingrese un numero: ")
    
    while calculando:
        if numero1.isdigit():
            numero1 = int(numero1)
            break
        elif numero1[0] == "-" and numero1[1:].isdigit():
            numero1 = int(numero1)
            break
        else:
            print("valor no valido")
            numero1 = input("Ingrese un numero: ")
    numero2 = input("Ingrese otro numero: ")
    while calculando2:
        if numero2.isdigit():
            numero2 = int(numero2)
            break
        elif numero2[0] == "-" and numero2[1:].isdigit():
            numero2 = int(numero2)
            break
        else:
            print("valor no valido")
            numero2 = input("Ingrese otro numero: ")

    numero1 = int(numero1) / 10 
    numero2 = int(numero2) / 10  
    print(f"{numero1} + {numero2} = {devuelveSuma(numero1, numero2):.1f}")
    print(f"{numero1} - {numero2} = {devuelveResta(numero1, numero2):.1f}")
    print(f"{numero1} * {numero2} = {devuelveMultiplicacion(numero1, numero2):.1f}")
    print(f"{numero1} / {numero2} = {devuelveDivision(numero1, numero2):.2f}")
"""


