# Uso del Return en las funciones
# Así cuando llamamos a la función almacenamos el resultado en una variable
# Permitiendo que la podamos usar más adelante en el código
# Mientras que print solamente muestra resultado en pantalla sin almacenarlo
def convertir_segundos(seconds):
    horas = (seconds // 3600)
    minutos = (seconds - horas * 3600) // 60
    segundos_restantes = seconds - horas * 3600 - minutos * 60
    return horas, minutos, segundos_restantes
# Al llamar a return nos devolverá en una variable los valores 
horas, minutos, segundos=convertir_segundos(4000)
# Podemos separar variables en una sola línea con comas
# En este caso es necesario porque la función devuelve 3 valores
print(horas, minutos, segundos)