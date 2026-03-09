# La regla de oro: usar "with".
# Cuando abres un archivo, debes cerrarlo al terminar.
# La forma más segura y simple es usando with + as f.
# Ejemplo de crear y escribir un archivo.

with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("Programa\n")
    f.write("Python\n")
    f.write("Archivos\n")
    f.write("Fin\n")
    
# Leer el contenido del archivo.

with open("notas.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
print(contenido)