# codewars kata: 4-letter names
def lista(x):
    lista = []
    for i in range(0,len(x)):
        if len(x[i]) == 4:
            lista.append(x[i])
    return lista

nombres = ['Samuel', 'Devany', 'Elianys', 'Michel', 'Paul']
print(lista(nombres))