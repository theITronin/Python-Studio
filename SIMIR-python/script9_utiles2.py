#    ██╗   ██╗████████╗██╗██╗     ███████╗███████╗    ██████╗ 
#    ██║   ██║╚══██╔══╝██║██║     ██╔════╝██╔════╝    ╚════██╗
#    ██║   ██║   ██║   ██║██║     █████╗  ███████╗     █████╔╝
#    ██║   ██║   ██║   ██║██║     ██╔══╝  ╚════██║    ██╔═══╝ 
#    ╚██████╔╝   ██║   ██║███████╗███████╗███████║    ███████╗
#     ╚═════╝    ╚═╝   ╚═╝╚══════╝╚══════╝╚══════╝    ╚══════╝
                                                         


# strip() / lstrip() / rstrip() What it does: removes blank spaces
# It doesn't touch what's in the middle

# strip: removes spaces from the left and right
# lstrip: removes spaces from the left
# rstrip: removes spaces from the right

t = "  Hola, Mundo  "
print(t.strip()) # "Hola, Mundo"
print(t.lstrip()) # "Hola, Mundo  "
print(t.rstrip()) # "  Hola, Mundo"
