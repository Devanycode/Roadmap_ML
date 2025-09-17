# Quiero entender cómo funciona esto

def hablaralto(texto):
    return texto.upper()

def hablarbajo(texto):
    return texto.lower()

def hola(func):
    texto = func(input("Escribe algo"))
    print(texto)

hola(hablaralto)