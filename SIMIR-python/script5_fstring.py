#    ███████╗███████╗████████╗██████╗ ██╗███╗   ██╗ ██████╗ 
#    ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║████╗  ██║██╔════╝ 
#    █████╗  ███████╗   ██║   ██████╔╝██║██╔██╗ ██║██║  ███╗
#    ██╔══╝  ╚════██║   ██║   ██╔══██╗██║██║╚██╗██║██║   ██║
#    ██║     ███████║   ██║   ██║  ██║██║██║ ╚████║╚██████╔╝
#    ╚═╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

# f-strings

# Una f-string (desde Python 3.6) es una cadena que empieza con f o F
# y permite incrustar expresiones de Python entre llaves {}.
# Esas expresiones se evalúan y su resultado se convierte en texto.

nombre = "Diego"
print(f"Hola {nombre}") # "Saluda a Diego"
edad = 17
print(f"{nombre} tiene {edad} años") # "Años de Diego"