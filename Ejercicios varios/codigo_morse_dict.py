

morse = {
    "A": "·—", 
    "B": "—···",
    "C": "—·—·",
    "D": "————",
    "E": "—··",
    "F": "·",
    "G": "··—·",
    "H": "——·",
    "I": "····",
    "J": "··",
    "K": "·———",
    "L": "—·—",
    "M": "·—··",
    "N": "——",
    "Ñ": "—·",
    "O": "——·——",
    "P": "———",
    "Q": "·——·",
    "R": "——·—",
    "S": "·—·",
    "T": "···",
    "U": "—",
    "W": "··—",
    "X": "···—",
    "Y": "·——",
    "Z": "—··—",
}

morse_reverso = {}

for x in morse:
    valor = morse[x]
    morse_reverso[valor] = x
 
print(morse_reverso)


def to_morse(texto):
    texto = texto.upper()
    resultado = ""
    for letra in texto:
        if letra in morse:
            resultado += morse[letra]
            resultado += " "
        else:
            resultado += "   "
    return resultado
pass

# ——· ——·—— —·— ·—  ·—·· — —— ———— ——·—— 

def to_texto(codigo):
    codigo = codigo.split(" ")
    resultado = ""
    rev = morse_reverso
    for simbolo in codigo:
        if simbolo in rev:
            resultado += rev[simbolo]
        else:
            resultado += " "
    return resultado.capitalize()
pass
#print(to_texto(input("Ingrese morse: ")))




