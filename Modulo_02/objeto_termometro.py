class Termometro():
    def __init__(self):
        self.__unidadM = "C"
        self.__temperatura = 0

    def conversor(self, temperatura, unidad):
        if unidad == "C":
            return f"{(temperatura * 9 / 5) + 32:.2}º F"
        elif unidad == "F":
            return f"{(temperatura - 32) * 5 / 9:.2}º C"

    
    def __str__(self):
        return f"{self.__temperatura}º {self.__unidadM} por defecto"


def validacion_temperatura(temp):
    try:
        temp = int(temp)
        return True
    except:
        return False
def temperatura(temp):
    while not validacion_temperatura(temp):
        print("Valor incorrecto")
        temp = input("Ingrese la temperatura:")
    return int(temp)

def validacion_unidad(unidad):
    unidad = str(unidad)
    unidad = unidad.upper()
    while unidad != "C" and unidad != "F":
        print("Valor incorrecto")
        unidad = input("Ingrese (C/F):").upper()
    return str(unidad)




c = Termometro()
t = input("Introduce temperatura: ")
temp = temperatura(t)
u = input("Introduce tipo de grados (C/F): ")
unidad = validacion_unidad(u)
print(c.conversor(temp, unidad))
