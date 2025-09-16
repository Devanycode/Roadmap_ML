# Par o Impar
def odd_or_even(number):
    return "Even" if number%2==0 else "Odd"
print(odd_or_even(int(input("ingrese un número: "))))

def get_size(width,height,depth):
    volume= width * height * depth
    surface_area= 2 * ((width * height) + (width * depth) + (height * depth))
    return surface_area, volume
w = int(input("Ingrese el ancho: "))
h = int(input("Ingrese el alto: "))
d = int(input("Ingrese la profundidad"))
print(get_size(w,h,d))