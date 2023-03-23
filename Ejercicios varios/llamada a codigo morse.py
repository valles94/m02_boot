import codigo_morse_dict

mensaje = input("Dime un texto: ")

telegrama = codigo_morse_dict.to_morse(mensaje)

print(telegrama)