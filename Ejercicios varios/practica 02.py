# programa que calcule total factura

def validacion(precio):
    try:
        float(precio)
        return True
    except:
        return False



def ingresar_productos(precio):
    while not validacion(precio):
        print(f"El valor {precio} no es válido")
        precio = input(f"Introduce un numero: ")
    if precio == "0":
        print()
    return precio

def plural(precio_a, product):
    total_unitario = precio_a * product
    if product == 1:
        print(f"{precio_a}€    -    {product} unidad    -    {total_unitario}€")
    else:
        print(f"{precio_a}€    -    {product} unidades    -    {total_unitario}€")
    

def plural_final(precio_a, product):
    total_unitario = precio_a * product
    if product == 1:
       return f"{precio_a}€    -    {product} unidad    -    {total_unitario}€\n"
    else:
        return f"{precio_a}€    -    {product} unidades    -    {total_unitario}€\n"


def Ticket():
    aImprimir = ""
    total_items = 0
    precio_total = 0
    while True:
        precio = input("Introduce el precio del producto: ")
        precio_a = ingresar_productos(precio)
        if precio_a == "0":
            break
        productos = input("Ingrese la cantidad de productos: ")
        product = ingresar_productos(productos)
        if product == "0":
            break
        precio_a = float(precio_a)
        product = float(product)
        total_unitario = precio_a * product
        aImprimir += plural_final(precio_a, product) 
        plural(precio_a, product) # si quito esta linea dejaria de salir antes de cada pregunta, dejando solo la de arriba saldria formateado como el ejercicio quiere
        total_items += product
        precio_total += total_unitario
    
    print(aImprimir)
    print("- - - - - - - -")
    print(f"Total: {precio_total}€")
    print(f"Unidades: {total_items}")
    print()


Ticket()



# version antes de meter en funcion el plural
"""def Ticket():
    total_items = 0
    precio_total = 0
    while True:
        precio = input("Introduce el precio del producto: ")
        precio_a = ingresar_productos(precio)
        if precio_a == "0":
            break
        productos = input("Ingrese la cantidad de productos: ")
        product = ingresar_productos(productos)
        if product == "0":
            break
        precio_a = float(precio_a)
        product = float(product)
        total_unitario = precio_a * product
        if product == 1:
            print((f"{precio_a}€    -    {product} unidad    -    {total_unitario}€"))
        else:
            print(f"{precio_a}€    -    {product} unidades    -    {total_unitario}€")
        total_items += product
        precio_total += total_unitario

    print("- - - - - - - -")
    print(f"Total: {precio_total}€")
    print(f"Unidades: {int(total_items)}")"""
    

# 
"""def Ticket():
    aImprimir = ""
    total_items = 0
    precio_total = 0
    while True:
        precio = input("Introduce el precio del producto: ")
        precio_a = ingresar_productos(precio)
        if precio_a == "0":
            break
        productos = input("Ingrese la cantidad de productos: ")
        product = ingresar_productos(productos)
        if product == "0":
            break
        precio_a = float(precio_a)
        product = float(product)
        total_unitario = precio_a * product
        aImprimir += f"{precio_a}€    -    {product} unidades    -    {total_unitario}€\n" 
        plural(precio_a, product) # si quito esta linea dejaria de salir antes de cada pregunta, dejando solo la de arriba saldria formateado como el ejercicio quiere
        total_items += product
        precio_total += total_unitario
    
    print(aImprimir)
    print("- - - - - - - -")
    print(f"Total: {precio_total}€")
    print(f"Unidades: {total_items}")
    print()"""
