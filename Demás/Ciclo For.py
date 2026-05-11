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
