
ejercicios = ["frontlever", "backlever", "pino", "fullplanch"]
archivo = "ejercicios_calistenia.txt"
i = 0

with open(archivo, "w", encoding="utf-8") as ej:
    while True:
        ej.write(ejercicios[i] + "\n")
        i += 1
        if i == len(ejercicios):
            break

with open(archivo, "r", encoding="utf-8") as ej:
    contenido = ej.read()
print(contenido)