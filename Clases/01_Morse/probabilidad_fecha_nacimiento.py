# calcular el año en el que naciste

nombre = input("Como te llamas?: ")
print("Hola,", nombre)
edad = int(input("Introduce tu edad:"))
año = int(input("Introduce el año actual:"))
mes = int(input("Introduce el mes actual:"))
dia = int(input("Introduce el dia actual:"))

mes_01 = 31
mes_02 = 28
mes_03 = 31
mes_04 = 30
mes_05 = 31
mes_06 = 30
mes_07 = 31
mes_08 = 31
mes_09 = 30
mes_10 = 31
mes_11 = 30
mes_12 = 31


if mes == 1:
    transcurridos = dia
elif mes == 2:
    transcurridos = mes_01 + dia
elif mes == 3:
    transcurridos = mes_01 + mes_02 + dia
elif mes == 4:
    transcurridos = mes_01 + mes_02 + mes_03 + dia
elif mes == 5:
    transcurridos = mes_01 + mes_02 + mes_03 + 30 + dia
elif mes == 6:
    transcurridos = mes_01 + mes_02 + mes_03 + 30 + 31 + dia
elif mes == 7:
    transcurridos = mes_01 + mes_02 + mes_03 + 30 + 31 + 30 + dia
elif mes == 8:
    transcurridos = mes_01 + mes_02 + mes_03 + 30 + 31 + 30 + 31 + dia
elif mes == 9:
    transcurridos = mes_01 + mes_02 + mes_03 + 30 + 31 + 30 + 31 + 31 + dia
elif mes == 10:
    transcurridos = mes_01 + mes_02 + mes_03 + 30 + 31 + 30 + 31 + 31 + 30 + dia
elif mes == 11:
    transcurridos = mes_01 + mes_02 + mes_03 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dia
else:
    transcurridos = mes_01 + mes_02 + mes_03 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dia

prob = (transcurridos / 365) * 100

nacimiento = año - edad
print(f"naciste en {nacimiento}, con una probabilidad del {prob}")
print(f"o en {nacimiento - 1}, con una probabilidad del {100 - prob}")