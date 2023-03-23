from tkinter import *
from tkinter import ttk

_heightBtn = 50 # esta variable se define como constante y es fija para guardar el tamaño del boton, pero si la cambiamos modificamos las medidas de todo el programa, es una manera de ahorrar tiempo y evitar errores
_widthBtn =  68 # esta variable se define como constante y es fija para guardar el tamaño del boton, pero si la cambiamos modificamos las medidas de todo el programa, es una manera de ahorrar tiempo y evitar errores

class Calculator(ttk.Frame): # creamos la clase calculadora que hereda de ttk.Frame, que lo que hace es crear un frame del mismo tamaño que la ventana que hemso creado en la clase MainApp
    def __init__(self, parent, **kwargs): # creamos el constructor de la clase, y al ser heredada en este caso tenemso que ponerle siempre el parent, que es el padre del que viene heredada dicha clase y a donde se va a anclar la ventana que se crea, añadimos los argumentos mediante diccionario al añadir los ** delante
        ttk.Frame.__init__(self, parent, height = kwargs["height"], width = kwargs["width"]) # iniciamos el constructor de la clase padre y le enviamos los argumentos que nos interesen, en este caso al ser diccionario hay que añadir clave y valor
        self.display = Display(self) # creamos la variable self.display que llama a la clase Display, para poder colocarla en la calculadora dicha clase
        self.display.place(x=0, y=0) # ubicamos la variable display que hemos creado en la posicion de la ventana que queremos


class Display(ttk.Frame): #creamos una clase que va a ser la pantalla, que hereda de ttk.Frame
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height =_heightBtn, width = _widthBtn * 4) # al llamar al constructor de la clase padre, en este caso en lugar de dejar abierto como en el anterior a un diccionario la altura y anchura, como queremos que sea fija y no se pueda modificar se la damos nosotros

        self.pack_propagate(0) #este mandato lo que hace es conseguir que el boton tenga el tamaño que nosotros queremos, no el que sale por defecto 
        s = ttk.Style() #creamos una variable para poder crear estilos nuevos, aunque ya viene por defecto los estilos de ttk
        s.configure("my.TLabel", font = "Helvetica 42") # con la opcion .configure, podemos crear estilos especificos, gracias a que hemos creado la variable anterior que servia para crear nuevos estilos a partir de unos ya de serie, ahora creamos el nomre "my.TLabel", al añadir el "my." delante de TLabel(estilo por defecto) le decimos al programa que es nuestro estilo
        ## seguimos con al linea anterior ## podemos añadir el tipo de fuente que queremos y el numero es el tamaño

        self.lblDisplay = ttk.Label(self, text = "0", style = "my.TLabel", anchor = E) # creamos una variable llamada self.lblDisplay que va a ser una label de ttk, pero cuando en los argumentos le añadimos "style" y le damos nuestro estilo, cogera las propiedades de label de ttk pero con nuestro estilo, el anchor es el punto de ancla y al ponerle E significa "Este" es decir, derecha
        self.lblDisplay.pack(side = TOP, fill = BOTH, expand = True) # la función .pack podría evitar tener que usar el .place y ubicarlo de manera manual, usando este metodo podemos decirle la posicion, "side = TOP" coloca arriba el boton, el "fill = BOTH" dice que el boton sea igual de ancho que la ventana creada, es decir coja todo el tamaño y el "expand = True" ??


class BotonCalculadora(ttk.Frame): #creamos una clase que hereda de ttk.Frame y nos va a servir para crear los botones en la app
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height = _heightBtn, width = _widthBtn )
    


class MainApp(Tk): # Creamos la clase MainApp que hereda de Tk para crear la ventana de la app
    def __init__(self): #creamos el constructor de MainApp
        Tk.__init__(self) #invocamos al cosntructor de "Tk" ya que es una clase heredada la que hemos creado
        self.title("Calculadora") # asignamos un nombre
        self.geometry("{}x{}".format(_widthBtn*4, _heightBtn*6)) # mediante el self.geometry asignamos el tamaño de la ventana que creamos, en este caso como tenemos el tamaño del boton en una variable, hacemos un format para no tener que poner numeros nosotros por evitar errores
        #dentro de la funcion del constructor, metemos la clase que hemos creado de calculator y le asignamos medidas y posicion
        self.calculator = Calculator(self, height = 300, width = 272) #creamos una variable que llama a nuestra clase Calculator y le damos las medidas que queremos
        self.calculator.place(x=0, y = 0) # mediante el .place ubicamos la posicion de la variable que hemos creado


    def start(self): # creamos la funcion start para iniciar la ventana
        self.mainloop()  # con la funcion self.mainloop() que viene heredada de Tk, lanzamos la ventana

if __name__ == "__main__": # creamos la condicion de que si imprimimos desde la ventana Main nos imprimira la app, si es invocada a traes de un import, no la imprimira
    app = MainApp()
    app.start() # llamamos a la funcion start() de la funcion MainApp para poder iniciar la app
        

