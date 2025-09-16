# Ejemplo de uso de las sentencias if, elif y else y las comparaciones
def contraseña_usuario(usuario):
    if len(usuario)<5:
        return("la contraseña debe tener más de 5 caracteres")
    elif len(usuario)>15:
        return("la contraseña debe tener menos de 15 caracteres")
    else:
        return("la contraseña es válida")
contraseña=contraseña_usuario("devanyrinconceballoscode")
print(contraseña)

def par_impar(número):
    if número % 2 == 0:     # % sirve para devolver el residuo de una división
        return("el número es par")
    else:
        return("el número es impar")
valor_número = par_impar(10)
print(valor_número)
