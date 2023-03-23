# PREPARACIÓN

def contarLetras(palabra, freq):
        for i in palabra:
            freq[i] = palabra.count(i)

def isAnagram(palabra1, palabra2):
    
    frecuencias1 = {}
    frecuencias2 = {}
            
    contarLetras(palabra1, frecuencias1)
    contarLetras(palabra2, frecuencias2)

    if  frecuencias1 == frecuencias2:
        return True
    else:
        return False


# ENTRADA

palabra1 = input("Primera palabra: ")
palabra2 = input("Segunda palabra: ")


# PROCESO

palabra1 = palabra1.upper()
palabra2 = palabra2.upper()

consulta = isAnagram(palabra1, palabra2)


# SALIDA

if consulta == True:
    print("Son anagramas.")
else:
    print("No son anagramas.")