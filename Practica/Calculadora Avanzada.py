import math

print("""
 
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝███████║
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
""") 

print("""
1.Suma
2.Resta
3.Multiplicación
4.División
5.Raíz 
6.Potencia
7.Fracciones
""")

op = int(input("Elije la operación: "))
num1 = int(input("Elije el primer número: "))
num2 = int(input("Elije el segundo número: "))


def suma(num1, num2):
    return num1 + num2
def resta(num1, num2):
    return num1 - num2
def multiplicación(num1, num2):
    return num1 * num2
def división(num1, num2):
    return num1 / num2
def raíz (num1, num2):
    return math.pow(num1, 1 / num2)
def potencia (num1, num2):
    return num1 ** num2
def fracciones (num1, num2):
    return num1 / num2

if op == 1:
    resultado = suma(num1, num2)
if op == 2:
    resultado = resta(num1, num2)
if op == 3:
    resultado = multiplicación(num1, num2)
if op == 4:
    resultado = división(num1, num2)
if op == 5:
    resultado = raíz(num1, num2)
if op == 6:
    resultado = potencia(num1, num2)
if op == 7:
    resultado = fracciones(num1, num2)
    
    
print("Este es el resultado:", resultado)

