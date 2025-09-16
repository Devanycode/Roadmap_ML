# Uso de While Loop y como se modifica la variable permanentemente
x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1 
# la variable x queda con el valor con el que salga del ciclo, en este caso es 10
product = 1
while x < 10:  # No se ejecutará el ciclo porque x ya es 10 ya que no se redefinió la variable
    product = product * x
    x = x + 1

print(sum, product)
#Ouput 45 1