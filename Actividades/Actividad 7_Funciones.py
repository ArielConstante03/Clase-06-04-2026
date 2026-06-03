#Actividad 7
def mostrar_estudiante(nombre, curso):
    print('Datos del Estudiante:')
    print('--------------------')
    print(f'Nombre: {nombre}')
    print(f'Curso: {curso}')
nombre = str(input("Ingrese el nombre del Estudiante: "))
curso = str(input("Ingrese el curso del Estudiante: "))
mostrar_estudiante(nombre, curso)

