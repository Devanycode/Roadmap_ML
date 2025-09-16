# Errores en bucles for
for x in 25:
    print(x)    # Será un error ya que no se puede iterar sobre un número 
# Para solucionarlo simplemente se hace 
for x in [25]:
    print(x)
for x in range(25):
    print(x)