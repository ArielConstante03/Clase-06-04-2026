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
