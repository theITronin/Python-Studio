
gastos = "gastos.txt"
gasto_hoy = str(input("Cuanto gastastes hoy?" + "\n"))

with open(gastos, "a", encoding="utf-8") as g:
    g.write(gasto_hoy + "\n")
    
with open(gastos, "r", encoding="utf-8") as g:
    lines = g.readlines()
print("Nº de Registros:", len(lines))