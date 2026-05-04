#Ariel Constante
#04 05 2026
#%%
#Actividad 1
VariableControl = 0
while VariableControl < 5:
    print("VariableControl:", VariableControl)
    VariableControl += 1
else:
    print(f"Variable de Control es: {VariableControl}") 
# %%
#Actividad 2
clave = input("Ingrese la clave: ")
while clave != "python":
    clave = input("Ingrese la clave: ")
print("Clave correcta")  # Clave correcta
# %%
#Actividad 3
opcion = ""
while opcion != "salir":
    print("Menú de opciones:")
    print("1. Saludar")
    print("2. Mostrar mensaje")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Hola, bienvenido")
    elif opcion == "2":
        print("Estamos aprendiendo ciclos While")
    elif opcion == "3":
        print("Saliendo del programa")
    else:
        print("Opción no válida, por favor intente de nuevo")
# %%
