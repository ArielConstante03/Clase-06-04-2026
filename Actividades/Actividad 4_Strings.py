#Ariel Constante
#17 04 2026
#Actividad 4 - Strings
#%%
# Nivel 1: Operaciones básicas
texto = "Programación Para Todos"
print(texto)
print(len(texto))
# %%
# Nivel 2: Transformación de texto
texto = "Programación Para Todos"
print(texto.upper())
print(texto.lower())
print(texto.title())
print(texto.capitalize())
# %%
# Nivel 3: Búsqueda y verificación
texto = "Programación Para Todos"
print(texto.startswith("Programación"))
print(texto.endswith("Todos"))
print(texto.find("Para"))
print("Python" in texto)
# %%
# Nivel 4: Manipulación
texto = "Programación Para Todos"
texto_reemplazado = texto.replace("Programación", "Python")
print(texto_reemplazado)
palabras = texto.split()
print(palabras)
print(" - ".join(palabras))
# %%
# Nivel 5: Índices
texto = "Programación Para Todos"
print(texto[0])
print(texto[-1])
print(texto[5])
# %%
# Nivel 6: Aplicación simple
nombre_completo = "Ariel Constante"
print(f"Hola, mi nombre es {nombre_completo}")
iniciales = "".join(p[0].upper() for p in nombre_completo.split() if p)
print(iniciales)
