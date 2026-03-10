# The golden rule: use "with".
# When you open a file, you should close it when you're finished.
# The safest and simplest way is by using with + as f.
# Example of creating and writing a file.

with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Program\n")
    f.write("Python\n")
    f.write("Files\n")
    f.write("Fin\n")
    
# Leer el contenido del archivo.

with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)