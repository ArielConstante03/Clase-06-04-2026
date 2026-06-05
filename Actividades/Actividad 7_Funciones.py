# Ariel Constante
# 03 06 2026

#%%
#Actividad 1
def mostrar_estudiante(nombre, curso):
    print('Datos del Estudiante:')
    print('--------------------')
    print(f'Nombre: {nombre}')
    print(f'Curso: {curso}')
nombre = str(input("Ingrese el nombre del Estudiante: "))
curso = str(input("Ingrese el curso del Estudiante: "))
mostrar_estudiante(nombre, curso)

#%%
#Actividad 2
def obtener_mensaje(mensaje):
    return mensaje
def generar_nombre_completo(nombre, apellido):
    nombre_completo = (f'{nombre} {apellido}')
    return nombre_completo
mensaje = str(input("Ingrese el mensaje: "))
nombre  = str(input("Ingrese el nombre: "))
apellido =  str(input("Ingrese el apellido: "))
print(f'{obtener_mensaje(mensaje)}, {generar_nombre_completo(nombre, apellido)}')

#%%
#Actividad 3
def suma (a, b):
    print (f'{a} + {b} = {a+b}')
    return suma
def resta (a, b):
    print (f'{a} - {b} = {a-b}')
    return resta
def multiplicación (a, b):
    print (f'{a} x {b} = {a*b}')
    return multiplicación
def división (a, b):
    print (f'{a} ÷ {b} = {a/b}')
    return división
def instrucciones ():
    print ('Este programa es una calculadora de las 4 operaciones básicas (+, -, x, ÷)')
    print ('\nLas instrucciones son: \n0 Para mostrar las instrucciones\n1 Para sumar \n2 Para restar \n3 Para multiplicar \n4 Para dividir \n5 Para salir')
print(instrucciones())
while True:
    elección = int(input("Su elección: "))
    if elección == 5:
        print('Programa finalizado correctamente')
        break
    elif elección == 0:
        print(instrucciones())
        elección =+ 6
    elif elección > 0 and elección < 5:
        a = float(input("Ingrese el primer número: "))
        b = float(input('Ingrese el segundo número: '))
        if elección == 1:
            print(suma(a, b))
        elif elección == 2:
            print(resta(a,b))
        elif elección == 3:
            print(multiplicación(a,b))
        elif elección == 4:
            print(división(a,b))
    else:
        print('Ingrese uno de los número mostrados...')

# Tarea 
# 05/06/2026
def promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def nota_mayor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

def nota_menor(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n1 and n2 <= n3:
        return n2
    else:
        return n3

def estado_estudiante(n1, n2, n3):
    prom = promedio(n1, n2, n3)
    
    if prom >= 7:
        return "Aprueba"
    else:
        return "Reprueba"
print('Este programa necesita tres notas')
nota1 = float(input("Ingrese la primera calificación: "))
nota2 = float(input("Ingrese la segunda calificación: "))
nota3 = float(input("Ingrese la tercera calificación: "))
while True:
    print("\nMENÚ\n1. Calcular promedio\n2. Mostrar nota mayor\n3. Mostrar nota menor\n4. Determinar si aprueba o reprueba\n5. Salir del programa")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 5:
        print('Programa finalizado correctamente')
        break
    else:
        if opcion == 1:
            print("Promedio:", promedio(nota1, nota2, nota3))
        elif opcion == 2:
            print("Nota mayor:", nota_mayor(nota1, nota2, nota3))
        elif opcion == 3:
            print("Nota menor:", nota_menor(nota1, nota2, nota3))
        elif opcion == 4:
            print("Resultado:", estado_estudiante(nota1, nota2, nota3))
        else:
            print("Opción no válida")
