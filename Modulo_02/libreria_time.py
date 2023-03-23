from time import gmtime, strftime  #importamos desde el modulo tiempo, la variable "strftime" que lo que hace es devolverte la fecha, actual, la cual se puede personalizar:

hoy = strftime("%d - %b - %Y") # con este formato personalizamos una variable con los datos que le decimos, "%d = día en numeros del mes", "%b = mes abreviado", "%Y en mayusculas = año entero(2023), si no pondria solo 23"

print(hoy)


