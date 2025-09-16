def saludo(nombre):   # Saludo es la función y nombre es el parámetro
    print("Hola ", nombre)
# Desde afuera se puede definir la función
saludo("Devany")
'''The function in this code is saludo. It takes one parameter,
nombre, and prints "Hola " followed by the value of nombre. 
For example, saludo("Devany") will print Hola Devany.'''

### En caso de que haya más de un parámetro.
def saludo(nombre, apellido):  # Saludo es la función y nombre y apellido son los parámetros
    print("Hola ", nombre, apellido)
print(saludo("Devany","Rincón")) 
'''Se llama a la función saludo() y se le da valor a sus parámetros 
también separados por comas.''