
exercise = ["frontlever", "backlever", "pino", "fullplanch"] # We define a list.
file = "sw_exercise.txt"
i = 0 # We initialize a var to 0.

with open(file, "w", encoding="utf-8") as ej: 
    while True:
        ej.write(exercise[i] + "\n") # We write the file using a while loop.
        i += 1
        if i == len(exercise):
            break

with open(file, "r", encoding="utf-8") as ej: 
    content = ej.read() # We read the content of the file
print(content)