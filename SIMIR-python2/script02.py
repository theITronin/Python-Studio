
# Creamos archivo y le ponemos como alias "f"
with open("nombres.txt", "w", encoding="utf-8") as f:
    f.write("Bryan ") # Escribimos todos estos nombres dentro del archivo
    f.write("Marco ")
    f.write("Eduardo ")
    f.write("Bruno ")
    f.write("Diego ")
    
# Abrimos el archivo y leemos el contenido.
with open("nombres.txt", "r", encoding="utf-8") as f:
    contenido = f.read() # Pasamos el contenido del archivo a una variable
print(contenido)