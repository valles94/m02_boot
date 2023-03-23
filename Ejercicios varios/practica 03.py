# tabla de conversion de grados C a F y viceversa 

peticion = input("Introduce C o F en función de la tabla que desee ver: ").upper()

def centigrados():
    cgrados = 0
    fgrados = 32
    while fgrados <= 230:
        cgrados = (fgrados - 32) * 5/9
        print(f"{cgrados:7.2f}ºC   ---   {fgrados:7.2f}ºF")
        fgrados += 10

def fahrenheit():
    cgrados = 0
    fgrados = 0
    while fgrados <= 100:
        cgrados = (fgrados - 32) * 5/9
        print(f"{fgrados:7.2f}ºF   ---   {cgrados:7.2f}ºC")
        fgrados += 10

def bucle(valor):
    while valor != "C" and valor != "F":
        valor = input("Valor incorrecto, vuelva a introducir F o C: ").upper()
    return valor


peticion = bucle(peticion)
if peticion == "C":
    centigrados()
else:
    fahrenheit()

    