# calcular el año en el que naciste

nombre = input("Como te llamas?: ")
print("Hola,", nombre)
edad = int(input("Introduce tu edad:"))
año_actual = int(input("Introduce el año actual:"))
cumpleaños = input("Has cumplido ya años? (S/N)").upper()
resta = año_actual - edad

if cumpleaños == "S":
    print(resta)
else:
    print(resta - 1)


