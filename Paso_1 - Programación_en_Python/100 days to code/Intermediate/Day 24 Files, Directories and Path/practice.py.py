r"""
file = open(r"C:\Users\devan\OneDrive\Documentos\Python\Roadmap_ML\Paso_1 - 
Programación_en_Python\100 days to code\Intermediate\Day 24 Files, Directories and Path\my_file.txt")
contents = file.read()   # Devuelve las cosas en una cadena 
print(contents)
file.close()    # El archivo consume datos, podemos decirle cuando cerrarse para que controlemos cuando liberar esos recursos
# Es como cerrar una ventana del navegador para no tener abiertas cosas innecesarias
"""



# RUTA ABSOLUTA
with open("/Users/devan/OneDrive/Escritorio/my_file.txt") as file:
    contents = file.read()
    print(contents)

# RUTA RELATIVA
# Este es Onedrive (el primero)
with open("../../../../../../../Escritorio/my_file.txt") as file:
    contents = file.read()
    print(contents)

