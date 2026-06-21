# We created a file and named it "f" as the alias.
with open("names.txt", "w", encoding="utf-8") as f:
    f.write("Bryan ") # We wrote all these names inside the file.
    f.write("Marco ")
    f.write("Eduardo ")
    f.write("Bruno ")
    f.write("Pablo ")
    
# We open the file and read the contents.
with open("names.txt", "r", encoding="utf-8") as f:
    contenido = f.read() # We write the file content into a var.
print(contenido)