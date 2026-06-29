"""- Añadir tareas (con descripción, prioridad y fecha)
- Marcar como completada
- Eliminar tareas
- Ver tareas pendientes y completadas
- Ver tareas ordenadas por prioridad o fecha"""
import functions 





for x in range(3):
    main = functions.greeting()
    if main == 1:
        functions.add_task()

    elif main == 2:
        functions.complete_task()
print(functions.tasks)




