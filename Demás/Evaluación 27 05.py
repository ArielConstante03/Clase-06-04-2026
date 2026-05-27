# Acceso con clave
clave_correcta = "1234"
clave = ""

while clave != clave_correcta:
    clave = input("Ingrese la clave de acceso: ")
    if clave != clave_correcta:
        print("Clave incorrecta, intente nuevamente.")

print("Acceso concedido\n")
