
expenses = "expenses.txt"
today_expenses = str(input("How much did you spend today?" + "\n"))

with open(expenses, "a", encoding="utf-8") as g: # We open a file with append format.
    g.write(today_expenses + "\n")
    
with open(expenses, "r", encoding="utf-8") as g: # We open a file with read format.
    lines = g.readlines()
print("Nº of Records:", len(lines))