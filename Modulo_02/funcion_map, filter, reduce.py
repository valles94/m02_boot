lista = [1, 3, 10, -2, 9]

listaDobles = map(lambda x: x * 2, lista) # la funcion "map()" lo que hace es aplicar la transformacion que hemos introducido mediante la funcion anonima "lambda" a cada uno de los objetos que hay en una lista por ejemplo
# Si en lugar de haber usado "lambda" usamos una funcion predefinida de primer nivel, haría exactamente lo mismo, aplicaria lo que se haga en la funcion a cada uno de los parametros de la lista

listaDobles = list(listaDobles) #convertimos la variable en una lista e imprimimos y nos devolvera la lista con los resultados tras haber aplicado el lambda

print(listaDobles)


lista = [1, 3, 10, -2, 9]

listaPares = filter(lambda x: x % 2 == 0, lista) # la funcion "filter()" lo que hace es filtrar en funcion de lo que le digamos a traves de una lambda, o a traves de una funcion
# en este caso le hemos dicho que todos los numeros que al dividir entre 2 sean de resto 0, nos los muestre, si no que pase, seria como hacer una funcion basica de condicional "if" que nos devolviese los pares, pero aqui usando una lambda

listaPares = list(listaPares)

print(listaPares)

from functools import reduce  # para usar la funcion "reduce" es necesario importarla ya que no viene como un estandar tipo "map" o "filter"

lista = [1, 3, 10, -2, 9]

sumatorio = reduce(lambda x, y: x + y, lista) # esta funcion reduce toda la lista a un unico valor, y ese valor va a depender de la operacion que hayamos dicho a traves de una lambda o una funcion
#OJO QUE EL REDUCE NO FUNCIONA BIEN CON ALGUNAS LAMBDAS SI NO SON FUNCIONES MUY SENCILLAS, NO ABUSAR DE SU USO Y ESTAR MUY SEGURO CUANDO SE USA

print(sumatorio)

