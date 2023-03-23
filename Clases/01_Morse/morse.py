
letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cadena = input("Ingrese una palabra: ").upper()
simbolos = ["·—", "—···","—·—·","————", "—··", "·","··—·","——·","····","··","·———","—·—","·—··","——","—·","——·——","———","·——·","——·—","·—·","···","—","··—","···—","·——","—··—","—·——","——··"]

for letra in cadena:
    posicion = 0
    while posicion < len(letras):
        l = letras[posicion]
        espacio = " "
        if l == letra:
            break
        posicion += 1
    if posicion == len(letras):
        print("no encontrado")
    else:
        print("{} = {}".format(letra, simbolos[posicion]))

