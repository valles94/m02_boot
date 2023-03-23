def esBisiesto(año):
    año = int(año)
    for x in range(1, año+1):
        if x % 4 == 0:
            print(f"{x} Es bisiesto")
        else:
            print(f"{x} No es bisiestos")


año = input("ingrese el año: ")

esBisiesto(año)