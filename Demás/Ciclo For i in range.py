# Ariel Constante
# 20/05/2026
# Ciclo For i in range
# Actividad 1: Tabla de multiplicar
num = int(input("Ingrese el número del que desea la tabla de multiplicar: "))
inicio = int(input("Ingrese el número desde el que desa iniciar la tabla de multiplicar: "))
fin = int(input("Ingrese el número hasta el que desea terminar la tabla de multiplicar: "))
for i in range (inicio, fin+1):
    print (f'{num} x {i} = {num*i}')

# Actividad 2: A una lista
notas = [5, 8, 9, 7, 10]
prom = 0
suma = 0
cantidad = 0
for i in range (1, 4):
    suma += notas [i]
    cantidad += 1
prom = suma/cantidad
print (f'El promedio de las notas 1, 2 y 3 es de: {prom}')

# Actividad 3: Incremento y decemento
num = int(input("Ingrese el número del que desea la tabla de multiplicar: "))
inicio = int(input("Ingrese el número desde el que desa iniciar la tabla de multiplicar: "))
if inicio%2 == 1:
    inicio += 1
fin = int(input("Ingrese el número hasta el que desea terminar la tabla de multiplicar: "))
for i in range (inicio, fin+1, 2):
    print (f'{num} x {i} = {num*i}')

# Actividad 4: Lista
estudiantes = ["Ana", "Luis", "María", "Carlos", "Sofía", "Mateo"]
num = 0
for i in range(0, 6, 2):
    num +=1
    pareja = estudiantes [i] + " y " + estudiantes [i+1]
    print (f'Pareja {num}: {pareja}')

# Actividad 5: 
print (f'Tienes 3 vidas.')
for i in range (2, 0, -1):
    print (f'Te quedan {i} vidas.')

# Actividad 6: Ciclo For anidado
for fila in range(1, 4):
    for computadora in range(1, 5):
        nombre = input('Ingrese el nombre del estudiante: ')
        print(nombre, 'asignado a Fila', fila,
              '- Computadora', computadora)

    print('Fin de la fila', fila)
