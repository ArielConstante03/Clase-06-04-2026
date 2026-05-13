# Ariel Constante
# 12 05 2026
# Actividad 7 - Ciclos For

#%%
#EJERCICIO LISTAS
notas = [8.5, 6.0, 9.0, 7.0, 5.5]
suma = 0
aprobados = 0
reprobados = 0
for nota in notas:
    suma = suma + nota
    if nota >= 7:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1
promedio = suma / len(notas)
print("La suma total de las notas es:", suma)
print("El promedio del curso es:", promedio)
print("La cantidad de estudiantes aprobados es:", aprobados)
print("La cantidad de estudiantes reprobados es:", reprobados)

#%%
#EJERCICIOS STRING
contrasena = "Python2026"
letras = 0
numeros = 0
cantidad_o = 0
for caracter in contrasena:
    if caracter.isalpha():
        letras = letras + 1
    if caracter.isdigit():
        numeros = numeros + 1
    if caracter == "o":
        cantidad_o = cantidad_o + 1
print("La cantidad de letras es:", letras)
print("La cantidad de números es:", numeros)
print("La cantidad de veces que aparece la letra o es:", cantidad_o)

#%%
#EJERCICIOS CON SET
productos = {"teclado", "mouse", "monitor", "mouse", "impresora"}
cantidad_productos = 0
productos_mayores = 0
for producto in productos:
    cantidad_productos = cantidad_productos + 1
    contador_letras = 0
    for letra in producto:
        contador_letras = contador_letras + 1
    if contador_letras > 6:
        productos_mayores = productos_mayores + 1
print("La cantidad de productos únicos es:", cantidad_productos)
print("La cantidad de productos con más de 6 letras es:", productos_mayores)

#%%
#EJERCICIO CON BREAK
correo = input("Ingrese su correo electrónico: ")
usuario = ""
for caracter in correo:
    if caracter == "@":
        break
    usuario = usuario + caracter
print("El nombre de usuario es:", usuario)

#%%
#EJERCICIO CON CONTINUE
telefono = input("Ingrese su número de teléfono: ")
telefono_limpio = ""
for caracter in telefono:
    if caracter == " " or caracter == "-":
        continue
    telefono_limpio = telefono_limpio + caracter
print("El número de teléfono limpio es:", telefono_limpio)
