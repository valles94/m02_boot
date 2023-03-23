from funciones_primer_nivel_return import sumatodos

# Al importar modulos externos, tenemos que acordarnos de poner el if "__name__", ya que si no nos imprimira todo lo que hay en el otro modulo, está explicado en el otro modulo

doble = lambda x: x * 2 # podemos definir una variable con una funcion anonima lambda para luego en el print no poner lambda sino poner la variable, ayuda en legibilidad

print(sumatodos(3, doble)) # funcionaria igual que el print de abajo pero con la variable que hemos creado

print(sumatodos(3, lambda x: x ** 3)) # el uso de las "lambda" son "funciones anonimas y vacias" que nos permiten hacer codigo despues del "x:"

