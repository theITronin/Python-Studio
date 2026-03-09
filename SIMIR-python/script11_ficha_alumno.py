#    ███████╗██╗ ██████╗██╗  ██╗ █████╗      █████╗ ██╗     ██╗   ██╗███╗   ███╗███╗   ██╗ ██████╗ 
#    ██╔════╝██║██╔════╝██║  ██║██╔══██╗    ██╔══██╗██║     ██║   ██║████╗ ████║████╗  ██║██╔═══██╗
#    █████╗  ██║██║     ███████║███████║    ███████║██║     ██║   ██║██╔████╔██║██╔██╗ ██║██║   ██║
#    ██╔══╝  ██║██║     ██╔══██║██╔══██║    ██╔══██║██║     ██║   ██║██║╚██╔╝██║██║╚██╗██║██║   ██║
#    ██║     ██║╚██████╗██║  ██║██║  ██║    ██║  ██║███████╗╚██████╔╝██║ ╚═╝ ██║██║ ╚████║╚██████╔╝
#    ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                              

nombre = str(input("Nombre: ").strip()) # Entrada para la variable nombre.
edad = int(input("Edad: ")) # Entrada para la varibale edad.
asignatura = str(input("Asignatura favorita: ").strip()) # Entrada para la variable asignatura.

print("-" * 30)

# Imprimimos un string + la variable correspondiente usando fstring.
print(f"Alumno/a: {nombre}") 
print(f"Edad: {edad}") 
print(f"Le encanta: {asignatura}")

print("-" * 30)