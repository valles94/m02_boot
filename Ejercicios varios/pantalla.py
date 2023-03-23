def clear():
    print("\033[2J") # Con este codigo, lo que hacemos es borrar el terminal, limpiar la pantalla

def locate(linea, columna):
    print("\033[{};{}H".format(linea, columna), end="") # Con esta funcion, al añadirle detras el .format, le indicamos donde queremos que envie nuestro cursor, al añadir detra el end= "" le decimos que termine la operacion con un espacio, si no saltaria de linea

def clearLine(linea = None, columna = None): # al añadir None por defecto, si no le damos datos limpiara la linea en la que se encuentre el cursor
    if linea is not None and columna is not None: # pero si le especificamos datos de linea y columna, nos limpiara la linea y columan que queremos
        locate(linea, columna)
    print("\033[K", end = "") # con esta funcion conseguimos borrar la linea donde lo apliquemos para que podamos seguir escribiendo encima

def format(style, colorText, colorBackground):
    print("\033[{};{};{}m".format(style,colorText, colorBackground), end = "")

def bold():
    print("\033[1m")
def regular():
    print("\033[0m")

def reset():
    print("\033[0m", end = "")


#explicacioni del .end
# de este modo nos lo imprime en 2 lineas
print("hola")
print("Caracola")

# de este otro modo nos lo imprime seguido, ya que hemos usado el .end
print("hola", end=" ")
print("caracola")

 