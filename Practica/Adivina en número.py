import random
from colorama import Fore, Style, init

print(f"""
 {Fore.MAGENTA}     
░█████╗░██████╗░██╗██╗░░░██╗██╗███╗░░██╗░█████╗░  ███████╗██╗░░░░░  ███╗░░██╗██╗░░░██╗███╗░░░███╗███████╗██████╗░░█████╗░
██╔══██╗██╔══██╗██║██║░░░██║██║████╗░██║██╔══██╗  ██╔════╝██║░░░░░  ████╗░██║██║░░░██║████╗░████║██╔════╝██╔══██╗██╔══██╗
███████║██║░░██║██║╚██╗░██╔╝██║██╔██╗██║███████║  █████╗░░██║░░░░░  ██╔██╗██║██║░░░██║██╔████╔██║█████╗░░██████╔╝██║░░██║
██╔══██║██║░░██║██║░╚████╔╝░██║██║╚████║██╔══██║  ██╔══╝░░██║░░░░░  ██║╚████║██║░░░██║██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░██║
██║░░██║██████╔╝██║░░╚██╔╝░░██║██║░╚███║██║░░██║  ███████╗███████╗  ██║░╚███║╚██████╔╝██║░╚═╝░██║███████╗██║░░██║╚█████╔╝
╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ╚══════╝╚══════╝  ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░
      """)
init(autoreset=True)

while True:
    nMaquina = random.randint(1, 10)
    while True:
        nUsuario = int(input(f"{Fore.LIGHTBLUE_EX}Adivina el número entre 1 y 10: "))

        if nUsuario < 1 or nUsuario > 10 or str(nUsuario):
            print(f"{Fore.LIGHTCYAN_EX}Número fuera de rango. Debe ser entre 1 y 10.")
            continue
        else:
            break
    if nMaquina == nUsuario:
        print(f"{Fore.LIGHTCYAN_EX}Ganaste!")
    else:
        print(f"{Fore.LIGHTCYAN_EX}Perdiste! El número era:", nMaquina)
        
    if str(input(f"{Fore.LIGHTBLUE_EX}¿Quieres jugar otra vez? Si o No: ").lower()) != 'si':
        print(f"{Fore.LIGHTBLUE_EX}Gracias por jugar!")
        break
    
   
        
