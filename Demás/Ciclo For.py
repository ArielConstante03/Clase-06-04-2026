# Ariel Constante
# 11 05 2026
# Ciclo For
#%%
#Actividad 1:
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

#%%
#Actividad 2:
notas = [8, 7, 9, 10, 6]
suma = 0
for nota in notas:
    suma = suma + nota
promedio = suma / len(notas)
print("El promedio es:", promedio)

# %%
#Actividad 3:
palabra = "Python"
for letra in palabra:
    print(letra)

#%%
#Actividad 4:
palabra = input("Ingrese una palabra: ")
print("La palabra es", palabra)
vocales = 0
for letra in palabra:
    if letra in "aeiouAEIOU":
        vocales = vocales + 1
print("El número de vocales es:", vocales)

#Extra: Cantidad de consonantes
consonantes = 0
letras_totales = int(len(palabra))
consonantes = letras_totales - vocales
print(f'La cantidad de consonantes es: {consonantes}')
print(f'La cantidad de letras total es: {letras_totales}')
#%%
#Actividad 5:
it_companies = {"Facebook", "Facebook", "Google", "Apple", "Amazon"}
for company in it_companies:
    print(company)

#%%
#Actividad 6:
asistentes = {"Ana", "Luis", "María", "Ana", "Carlos", "Luis", "Sofía"}
for estudiante in asistentes:
    print(f'Generar certificado para: {estudiante}')

#%%
#Actividad 7:
codigos = ['A-1101', 'A-1102', 'A-1103', 'A-1104', 'A-1105', ]
codigo_buscado = 'A-1103'
for codigo in codigos:
    print(codigo)
    if codigo == codigo_buscado:
        encontrado = True
        print(f'código encontrado: {codigo}')
        break

#%%
# Actividad 8: 
cedula = str(input("Ingrese su cédula: "))
cedula_limpia = ""
for caracter in cedula:
    if caracter == "-" or caracter == " ":
        continue
    cedula_limpia = cedula_limpia + caracter
print(f'La cédula limpia es: {cedula_limpia}')
# %%
