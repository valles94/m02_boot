def contador_inverso(e): # la recursividad es una funcion que es capaz de llamarse a si misma
    print(f"{e}, ", end= "")
    if e != 0:      # es necesaria para parar el bucle, ya que si no es un bucle infinito al estar llamandose a si misma continuamente
        contador_inverso(e-1) # de esta manera le hemos dicho que si "e" es diferente de 0 vuelva a llamarse, si es = a 0, corte
    

def sumatorio(numero):
    if numero > 0: 
        return numero + sumatorio(numero - 1)
    else:
        return 0

    

print(sumatorio(4))

def factorial(numero):
    if numero >= 1:
        return numero * factorial(numero - 1)
    else:
        return 1

print(factorial(5))


resultado = 1
for x in range(1,6):
    resultado *= x
   

print(resultado)
