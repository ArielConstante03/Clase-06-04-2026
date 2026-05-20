# Ariel Constante
# 20/05/2026
# Ciclo For i in range
# Actividad 1: Tabla de multiplicar
num = int(input("Ingrese el número del que desea la tabla de multiplicar: "))
inicio = int(input("Ingrese el número desde el que desa iniciar la tabla de multiplicar: "))
fin = int(input("Ingrese el número hasta el que desea terminar la tabla de multiplicar: "))
for i in range (inicio, fin+1):
    print (f'{num} x {i} = {num*i}')
