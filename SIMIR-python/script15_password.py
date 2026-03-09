# Declaración de variables
password = str(input("Ingrese su contraseña (8 caracteres mínimo): "))

# Condiciones
if len(password) < 8:
    print("La contraseña debe tener al menos 8 caracteres.")
else:
    print(f"Contraseña:{password} guardada")