class Dog():
    def __init__(self): #podemos crear un constructor vacio
        self.nombre = "" # es importante crear los atributos para que existan y luego poder modificarlos
        self.edad = None
        self.peso = None
    
    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma")
        if self.peso >= 8:
            print("GUAU GUAU")
        else:
            print("guau guau")

class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def ladrar(self):
        if self.peso > 8:
            print("GUAU GUAU")
        else:
            print("guau guau")

    def __str__(self):
        return f"Soy el perro {self.nombre}"
    
class PerroAsistencia(Perro): #al definir "Perro" dentro de esta segunda clse, le decimos a Python que "PerroAsistencia" es una subclase de Perro
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso) #invocando la clase Perro dentro de esta funcion, le decimos que el paso que hemos puesto arriba de self.nombre = nombre, funcione igual aqui
        self.amo = amo
        self.__trabajando = False # si añadimos __ delante de una palabra, convierte en "privado" ese valor y no podriamos cambiarlo desde fuera con la variable convirtiendola en True, tenemos que cambiarlo desde la funcion creada
    def __str__(self):
        return f"Soy el perro de asistencia {self.nombre} de {self.amo}"

    def pasear(self):
        print(f"Defiendo a mi dueño {self.amo}")

    def ladrar(self):
        if self.__trabajando:
            print("shhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
    def trabajando(self, valor = None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor

miko = Dog()
firulais = Perro("Firulais", 3, 5)
buster = PerroAsistencia("Buster", 5, 15, "Pablo")


print(miko.nombre)


print(firulais.nombre)
firulais.ladrar()
print(buster.nombre)
buster.ladrar()
buster.pasear()
# buster.trabajando = True # invocando esta funcion, cambiamos el estado de False por defecto qu ehabiamos establecido en su clase y ahora cambiaria su estado al ladrar
buster.trabajando(True) #al convertir la funcion trabajando en True, se convierte el self.__trabajando de False a True y nos devuelve el ladrido el else del ladrido
buster.ladrar()

