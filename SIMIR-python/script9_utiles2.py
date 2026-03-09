#    ██╗   ██╗████████╗██╗██╗     ███████╗███████╗    ██████╗ 
#    ██║   ██║╚══██╔══╝██║██║     ██╔════╝██╔════╝    ╚════██╗
#    ██║   ██║   ██║   ██║██║     █████╗  ███████╗     █████╔╝
#    ██║   ██║   ██║   ██║██║     ██╔══╝  ╚════██║    ██╔═══╝ 
#    ╚██████╔╝   ██║   ██║███████╗███████╗███████║    ███████╗
#     ╚═════╝    ╚═╝   ╚═╝╚══════╝╚══════╝╚══════╝    ╚══════╝
                                                         


# strip() / lstrip() / rstrip() Qué hace: quita espacios en blanco
# No toca lo que está en medio

# strip : elimina los espacios de la izquierda y de la derecha
# lstrip: elimina los espacios de la izquierda
# rstrip: elimina los espacios de la derecha

t = "  Hola, Mundo  "
print(t.strip()) # "Hola, Mundo"
print(t.lstrip()) # "Hola, Mundo  "
print(t.rstrip()) # "  Hola, Mundo"
