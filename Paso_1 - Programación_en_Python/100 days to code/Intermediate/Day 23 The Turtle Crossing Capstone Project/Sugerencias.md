- En vias.py: El for y in range(15) (15 vías) y for x in range(20) (20 dashes por vía) —estos números están relacionados con height/intervalos, pero si cambias pantalla, tienes que editarlos manualmente. No es grave (funciona), pero rompe flujo si escalas (e.g., más vías).

- En car_manager.py: if randint(0,10) > self.car_probability (0-10 fijo) —bien, pero si ajustas probabilidad, el rango podría no equilibrar (e.g., usa 0-100 para precisión).

- En scoreboard.py: Posición fija (-275, 230) —relacionada con pantalla, pero si width cambia, se desalinea.


Imports y Globals: Bien agrupados, pero considera orden alfabético (PEP 8) para legibilidad (e.g., from car_manager import ... antes de from player import ...).


### Puedo ser aún mejor con las constantes y valores hardcodeados.
### A la hora de importar se hace en orden alfabético, las constantes en orden lógico y sus nombres tienen que seguir la misma lógica cuando son del mismo tema

### Es mejor colocar dos bucles diferentes en lugar de un bucle sobre otro para mejores resultados
def draw_dashed_line(self, length):
    for x in range(length):
        self.pendown()
        self.forward(FORWARD_SIZE)
        self.penup()
        self.forward(FORWARD_SIZE)

# En creation_pathways:
for y in range(15):
    self.draw_dashed_line(20)  # 20 dashes
    self.coordinatey += INTERVAL_POSITION
    self.goto(self.coordinatex, self.coordinatey)