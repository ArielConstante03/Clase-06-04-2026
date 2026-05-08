#Ariel Constante & Sebastián Lara
#08 05 2026
#Actividad 1 - While con variable de control
n = 0
sumatotal = 0
n = int(input("Ingrese número entero positivo: "))
if n > 0:
    while n >= 0:
        sumatotal += n
        n -=1
    print (f'La suma total es {sumatotal}')
else:
    print ("No válido")

#%%
#Actividad 2 - While con break
precio = 1
suma = 0
while precio > 0:
    precio = int(input("Ingrese precio"))
    suma += precio
    if precio <= 0:
        print("El valor del registro de compras es de: $", suma)
        print("El programa ha finalizado")
        break
# %%
