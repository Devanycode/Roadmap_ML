options =  """1. Añadir una tarea.
2. Marcar como completada una tarea.
3. Eliminar alguna tarea.
4. Ver las tareas pendientes
5. Ver las tareas completadas.
6. Ver tareas ordenadas por prioridad o fecha
7. FINALIZAR EL PROCESO."""

tasks = {"Pendiente": {},
        "Completado": {}}

def greeting():
    return int(input("Hola, espero estés bien, presiona uno de los "
            f"siguientes números si quieres hacer algo:\n{options}\n"))
          
def add_task(): 
    """ Añade una tarea nueva al diccionario de tareas"""
    task_name = input("¿Qué nombre le quiere poner a su tarea?      ").strip()
    description = input("Descripción      ").strip()
    date = input("Fecha (ej: 2025-06-16)       ").strip()
    
    
    if tasks["Pendiente"] and tasks["Completado"]:
        task_number = max(max((tasks["Pendiente"].keys())), 
                          max((tasks["Completado"].keys()))) + 1
    elif tasks["Pendiente"]:
        task_number = max((tasks["Pendiente"].keys())) + 1
    elif tasks["Completado"]:
        task_number = max((tasks["Completado"].keys())) + 1
    else:
        task_number = 1
            
    tasks["Pendiente"][task_number] = {
        "Nombre": task_name,
        "Descripcion": description,
        "Fecha": date
    }

    print(f"✅ Tarea '{task_name}' añadida correctamente con ID {task_number}\n")

def complete_task():
    """Elimina la tarea de 'Pendiente' y la pasa a el estado de 'Completado'"""
    if tasks["Pendiente"].values():
        print("Estas son sus tareas en estado pendiente:\n")
        for task in tasks["Pendiente"]:
            print(tasks["Pendiente"][task])

        id_task = int(input("¿Cuál es el ID de la tarea que completó?"))
        if id_task in list(tasks["Pendiente"].keys()):
            tasks["Completado"][id_task] = tasks["Pendiente"][id_task]
            print(f"""✅ Se ha cambiado correctamente el estado de la tarea'
                  {tasks["Pendiente"][id_task]["Nombre"]}' con ID: {id_task}.\n""")
            tasks["Pendiente"].pop(id_task)
            print("Se ha eliminado su estado de 'Pendiente'.")
    else:
        print("Usted no tiene tareas pendientes, por ende no puede cambiar su estado.")        
    
    