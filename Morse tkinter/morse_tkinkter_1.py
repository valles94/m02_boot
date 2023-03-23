import morse_2
from tkinter import * #aqui importamos toda la libreria Tkinter
from tkinter import ttk  # aqui importamos un modoulo adicional de Tkinter que sirve para poner la estetica del sistema operativo, es necesario ponerlo aunque hayamos importado todo el proyecto en la linea anterior

class Translator(ttk.Frame): # la clase Translator hereda de "ttk.Frame", que es un rectangulo del tamaño que yo quiera, y modificable
    def __init__(self, padre, **kwargs): #esta funcion, nos pide siempre el "padre", que significa a donde voy a anclar el rectangulo que creo con el "ttk.Frame" y el parametro "**kwargs" que es un diccionario, es decir los aceptara siempre y cuando tengan clave y valor
        ttk.Frame.__init__(self, padre, height = kwargs["altura"], width = kwargs["ancho"]) #al ser una clase heredada hay que llamar al constructor de la clase original, ademas le pasaremos los parametros que queremos, en este caso le pasamos los valores del diccionario que nos interesan

        self.traduccionDirecta = True #creamos un interruptor para luego usarlo al traducir

        self.sender = StringVar() # el self.sender invocando a StringVar, nos declara una variable de tipo cadena
        self.receiver = StringVar()

        sender_lbl = ttk.Label(self, text = "Sender:", width=11, anchor=W) #creamos una label invocando ttk.label, y dandole los valores que queremos, el "anchor" es el punto de ancla, y la "W" significa izquierda. AQUI NO LE PONEMOS SELF. DELANTE PORQUE ES UN VALOR FIJO Y NO SE VA A MODIFICAR NI ACCEDER A EL
        sender_lbl.place(x=12, y=12) # con esta funcion lo que hacemos es ubicar la etiqueta que hemos creado antes, si no la ubicamos no aparece
        self.sender_entry = ttk.Entry(self, width=16, textvariable = self.sender) # el ttk.Entry, permite crear una caja para la entrada de texto de 1 sola linea, el textvariable = self.sender almacena el texto que hemso creado en la variable self.sender
        self.sender_entry.place(x=70, y= 10)


        receiver_lbl = ttk.Label(self, text = "Receiver:", width = 11, anchor = W)
        receiver_lbl.place(x=320, y=12)
        self.receiver_entry = ttk.Entry(self, width= 16, textvariable = self.receiver) # el valor width, significa la longitud de la caja de texto
        self.receiver_entry.place(x = 388, y = 10)


        self.origin_lbl = ttk.Label(self, text = "Plano", width = 5, anchor=W) # en estas 2 lineas hemos creado la etiqueta Origin con su texto y su ubicacion
        self.origin_lbl.place(x = 12, y = 40)
        self.origin_text = Text(self, width=35, height=8)  # En estas lineas hemos creado un campo de texto donde meter el texto que vamos a traducir, la funcion Text es un campo multilinea, por eso no hemos usado Ttk.Entry, que es solo de 1linea
        self.origin_text.place(x = 12, y = 60) # aqui lo ubicamos en la pantalla


        self.destino_lbl = ttk.Label(self, text = "Morse", width=12, anchor = W)
        self.destino_lbl.place(x = 320, y = 40)
        self.destino_text = Text(self, width=35, height=8)
        self.destino_text.place(x = 320, y = 60 )


        boton_send = ttk.Button(self, command = self.send_telegram, text="Send") #Creamos un boton con la funcion ttk.Buton() llamandose a si mismo, y añadiendo un texto y el command qeu es la funcion que debe hacer
        boton_send.place(x = 490, y = 170)

        boton_change = ttk.Button(self, command = self.chageText, text = "< = >")
        boton_change.place(x =395, y = 170)

        boton_traduce = ttk.Button(self, command = self.traduce, text = "Traducir")
        boton_traduce.place(x = 300, y = 170)

    def chageText(self):
        texto_original = self.origin_text.get("1.0", END) #asignamos a una variable el texto original y con el metodo .get("1.0", END) le decimos que nos coja desde el indice 0 hasta el final del texto para traducir
        texto_destino = self.destino_text.get("1.0", END)  #asignamos a una variable el texto destino y con el metodo .get("1.0", END) le decimos que nos coja desde el indice 0 hasta el final del texto para traducir
        if self.traduccionDirecta == True: # este es el interruptor que habiamos configurado al principio nos permite modificar para hacer el cambio
            self.origin_lbl.config(text = "Morse")  # usando el .config(text = "") hacemos el cambio de un lado del texto al otro para la traduccion
            self.destino_lbl.config(text = "Plano") 
            traduccion = morse_2.to_texto(texto_destino) # creamos la variable traduccion que es equivalente al modulo importado "morse_2" dentro de ese llamamos a su funcion "t_texto" ala que le introducimos la variable del texto original que hemos creado antes
        else:
            self.origin_lbl.config(text = "Plano") 
            self.destino_lbl.config(text = "Morse") 
            traduccion = morse_2.to_morse(texto_original) 
        self.destino_text.delete("1.0", END) # con este aprametro borramos el texto de destino cada vez que le damos a "intercambiar" 
        self.destino_text.insert(INSERT, texto_original) # con este prametro, insertamos el texto que habiamos traducido del cuadro destino al cuadro origen
        self.origin_text.delete("1.0", END) # con este aprametro borramos el texto de origen cada vez que le damos a "intercambiar"
        self.origin_text.insert(INSERT, texto_destino) # con este prametro, insertamos el texto que habiamos traducido del cuadro origen al cuadro destino
        print(traduccion)
        self.traduccionDirecta = not self.traduccionDirecta # NO VALE PONER FALSE, TIENE QUE SER ASI, ya que si ponemos False se qeudaria siempr een False, si ponemos esta variable, le decimos que se convierta al inverso del estado en el que venga, si viene en True se convertira en False y viceversa

    def traduce(self): #creamos una funcion para traducir el texto
        texto_original = self.origin_text.get("1.0", END) #asignamos a una variable el texto original y con el metodo .get("1.0", END) le decimos que nos coja desde el indice 0 hasta el final del texto para traducir
        if self.traduccionDirecta == True: # igual que en la funcion de changeText hace funcion de interruptor para saber cuando tiene que traducir de un texto a otro
            traduccion = morse_2.to_morse(texto_original) # creamos la variable traduccion que es equivalente al modulo importado "morse_2" dentro de ese llamamos a su funcion "to_morse" ala que le introducimos la variable del texto original que hemos creado antes
        else:
            traduccion = morse_2.to_texto(texto_original)
        self.destino_text.delete("1.0", END) # con este aprametro borramos el texto de destino cada vez que le damos a "traducir" para que nos muestre el nuevo texto
        self.destino_text.insert(INSERT, traduccion) # con este prametro, insertamos el texto que vamos a traducir en el cuadro de destino
        print(traduccion)

    def send_telegram(self):
        print("Enviar telegrama")


class MainApp(Tk):  #Creamos una clase llamada MainApp que hereda de la clase TK, sirve para crear ventanas. OJO, no ttk importado despues!! 
    def __init__(self):
        Tk.__init__(self) #al ser una clase heredada, tenemos que llamar al constructor de la clase original
        self.title("Traductor Morse") # Asignamos un nombre a nuestra clase??
        self.geometry("600x200") # creamos el tamaño de la ventana, para crearlo tenemos que invocar a geometry y darle como su fuese un string el tamaño deseado

        self.translator = Translator(self, altura = 200, ancho = 600) # de este modo creamos una ventana del mismo tamaño que la original de MainApp
        self.translator.place(x=0, y=0)  #de este modo anclamos al punto 0,0 nuestra ventana nueva de Translator
        

    def start(self):
        self.mainloop() # esta funcion, "self.mainlopp()" viene heredada de Tk y lo que hace es lanzar la ventana
    
if __name__ == "__main__":
    miTraductor = MainApp()
    miTraductor.start()
    



