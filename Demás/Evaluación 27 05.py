# Actividad de evaluación
clave_correcta = "python123"
clave = ""

while clave != clave_correcta:
    clave = input("Ingrese la clave de acceso: ")
    if clave != clave_correcta:
        print("Clave incorrecta, intente nuevamente.")

print("Acceso concedido\n")

print("Temas evaluados en la unidad:")
print("- variables")
print("- cálculos")
print("- input")
print("- print")
print("- f-string")
print("- condicionales")
print("- ciclos\n")

n = int(input("Ingrese la cantidad de estudiantes a revisar: "))

for i in range(n):
    print(f"\nRegistro del estudiante {i+1}")
    
    nombre = input("Ingrese el nombre del estudiante: ")
    nota1 = float(input("Ingrese la nota de ejercicios básicos: "))
    nota2 = float(input("Ingrese la nota de condicionales: "))
    nota3 = float(input("Ingrese la nota de ciclos: "))
    practicas = int(input("Ingrese la cantidad de prácticas completadas: "))
    
    promedio = (nota1 + nota2 + nota3) / 3
    
    if promedio >= 9 and practicas >= 5:
        estado = "Habilitado con nivel alto"
    elif promedio >= 7 and practicas >= 4:
        estado = "Habilitado"
    elif promedio >= 7 and practicas < 4:
        estado = "Pendiente por prácticas"
    else:
        estado = "Requiere refuerzo"
        
    print("\nReporte del estudiante")
    print(f"Nombre: {nombre}")
    print(f"Promedio final: {promedio}")
    print(f"Prácticas completadas: {practicas}")
    print(f"Estado académico: {estado}")

print("\nProceso finalizado")
