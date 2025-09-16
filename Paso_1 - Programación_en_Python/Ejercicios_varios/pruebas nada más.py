palabra = "Santiago"
print(f"{palabra:>10.2s}")
print(palabra)
numero = 3.182918811990
print("{:.2f}".format(numero))

tupla = ("samuel", "devany", "rincon")
for index, values in enumerate(tupla):
    print(str(index) + " - " + values)