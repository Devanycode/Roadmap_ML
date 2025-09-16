# Uso de Zip para recorrerlo

nombres = ["Ana", "Luis", "Carlos"]
edades = [20, 25, 30]

for nombre, edad in zip(nombres, edades):
    print(nombre, "tiene", edad, "años")
    
# También se puede comprimir el resultado en una lista
unidos = [nombre + " tiene " + str(edad) + " años" for nombre, edad in zip(nombres, edades)]
print(unidos)

