# Area de un triangulo

def esDigito(numero):
    try:
        float(numero)
        return True
    except:
        return False
    
base = input("Introduce la base: ")
while not esDigito(base):
    print(f"{base} debe ser un numero")
    base = input("Introduce la base: ")

altura = input("Introduce la altura: ")
while not esDigito(altura):
    print(f"{altura} debe ser un numero")
    altura = input("Introduce la altura: ")

area = (float(base) * float(altura)) / 2
print(f"El área del triangulo es: {area}")