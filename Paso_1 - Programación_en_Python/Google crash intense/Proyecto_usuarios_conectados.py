# Final Proyect 
def get_event_date(event):
    return event.date   # Se toma el evento como un objeto de tipo fecha

def current_users(events):
    events.sort(key = get_event_date)   # Se ordenan los eventos en el orden en que suceden (antes--> después)
    machines = {}   # Aquí es donde vamos a almacenar los usuarios en cada máquina
    for event in events:
        """Vamos a hacer un conteo para comprobar si ya está el valor, o si lo debemos agregar"""
        if event.machine not in machines:
            machines[event.machine] = set() # Si no está, lo agregaremos como un conjunto vacío en el que no se repiten valores
            """En este caso, se supone que los valores que son de classe event contienen ciertas características
            y se accede a estas con un punto después de mencionar la clase"""
        if event.type == "login":
            machines[event.machine].add(event.user) # Para agregar nuevos valores a un set() se usa el add
        elif event.type == "logout":
            if event.user in machines[event.machine]:
                machines[event.machine].remove(event.user)  # Aquí se eliminaría al usuario del diccionario debido a que ya cerró sesión
    """Aquí ya habríamos analizado todas las máquinas y agregado todos los usuarios que están en ellas en el momento actual"""
    return machines 

def generate_report(machines):
    """Esta función es para definir cómo vamos a devolver los valores al usuario"""
    for machine, users in machines.items():
        if len(users) > 0:  # Aquí verificamos que sólo imprima una máquina cuando tenga usuarios conectados
            user_list = ",".join(users) # Los nombres los usuarios van a estar separados por comas
            print(f"{machine}: {user_list}")    # Así le decimos en qué forma se imprimirá el resultado

class Event:
  def __init__(self, event_date, event_type, machine_name, user):   # Definimos los parámetros que tendrá la clase
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
  Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
  Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
  Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
  Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
  Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
  Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)