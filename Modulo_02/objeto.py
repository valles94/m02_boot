class Perro():  # las clases se crean siempre con la primera letra en Mayuscula
    # El primer objeto de la clse, siempre tiene que ser "SELF"
    def __init__(self, nombre, edad, peso): # creamos una funcion constructora y agregamos los parametros que queremos que tenga nuestro objeto Perro
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
# los atributos "self." y detras el nombre que hemos puesto en los parametros, lo que hacemos es decirle que el mismo tiene ese valor y responde a esos nombres
    def ladrar(self):
        if self.peso >= 8: # Si ponemos esta condicion, y tenemos mas de 1 perro creado, dpenede del peso que le hayamso dado al perro ladrara de un amanera o de otra
            print("GUAU, GUAU")
        else:
            print("Guau, Guau")

# con esta funcion, definimos un valor predeterminado, y en caso de que no llamemos a la funcion en el print, dandole un parametro, nos saldra un mensaje que hemos puesto nosotros 
    def __str__(self): # por ejemplo, si llamamos a imprimir print(firulais) pero no ponemos detras del objeto el ".nombre" o el atributo, nos devolvera este mensaje, si ponemos algun atributo nos deolvera el atributo y esta funcion la omitira
        return f"Soy el perro {self.nombre}"


firulais = Perro("Firulais", 3, 6)
mika = Perro("Mika", 5, 9)


print(firulais.nombre)
firulais.ladrar()
print(mika.nombre)
mika.ladrar()