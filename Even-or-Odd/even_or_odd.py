from colorama import Fore, Style

while True:
    num = int(input(f"{Fore.LIGHTMAGENTA_EX}Elije un número: "))
    if num % 2 == 0:
        print(f"{Fore.LIGHTCYAN_EX}El número es par")
    else:
        print(f"{Fore.LIGHTCYAN_EX}El número es impar")
    if str(input(f"{Fore.LIGHTMAGENTA_EX}¿Quieres jugar otra vez? (si/no) ")).lower() != "si":
        print (f"{Fore.LIGHTCYAN_EX}Gracias por jugar") 
        break
    