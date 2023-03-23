def normal(x):
    return x

def cuadrado(x):
    return x * x


def sumatodos(limite, f): # podemos utilizar funciones dentro de funciones
    resultado = 0
    for x in range(0, limite + 1):
        resultado += f(x) # en este ejemplo lo que le decimos es que al resultado se le sume lo que haya ocurrido en la funcion que le hemos dado al llamarla a imprimir
    return resultado



# CONSEGUIR EL VALOR MAAXIMO INTRODUCIDO
def max(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for x in range(0, len(l)):
        if l[x] > m:
            m = l[x]
    return m



# PODRIA SER OTRA MANERA DE CONSEGUIR EL VALOR MAS ALTO INTRODUCIDO

def max2(*arg):
    if len(arg) == 0:
        return 0
    arg = list(arg)
    arg.sort()
    mayor = arg[len(arg)- 1]
    return mayor



def media(*arg):
    if arg == 0:
        return 0
    suma = 0
    for x in arg:
        suma += x
    media = suma / len(arg)
    return media



funciones = {
    "max" : max,
    "max2" : max2,
    "normal": normal,
    "cuadrado": cuadrado,
    "media": media
}


def returnF(nombre):        # CON ESTA FUNCION, creamos una funcion que llama a funciones que las hemos metido en un dict
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    return None


# IMPORTANTE: CUANDO CREAMOS UN MODULO QUE ES PARA DEFINIR FUNCIONES E IMPORTARLO EN OTRO MODULO, TENEMOS QUE PONER ESTE APARTADO, YA QUE SI NO AL IMPORTAR EL MODULO EN UNO NUEVO E IMPRIMIR, NOS IMPRIMIRA TAMBIEN Ttodo EL CODIGO QUE TENGAMOS AQUI
if __name__ == "__main__":
    print(sumatodos(3, cuadrado))
    print(max(1,20,6,2,3,-15,9))
    print(max2(1,20,6,2,3,-15,9))
    print(media(1,20,6,2,3,-15,9))
    print(returnF("max")(1,20,6,2,3,-15,9)) # al imprimirla, le damos el nombre d euna de las claves del dict y luego le añadimos los parametros y esta funcion llamara a la funcion que hemos dicho para qu eno sdevuelva el valor
else:
    print("ejecutando modulo externo") # Este "else" con esta frase es opcional solo para que en la prueba que he hecho pueda ver que es correcto que no se imprime nada ahi

    
