# Convertidor de Celcius a Fahrenheit bien alineado
def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(f"{x:>3} F | {to_celsius(x):>6.2f} C")