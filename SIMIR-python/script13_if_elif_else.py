
# grade variable
nota = float(input("Nota del 0-10: "))

# conditionals
if nota < 0 or nota > 10:
    print("Nota inválida")
elif nota < 5:
    print("Clavado")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")


