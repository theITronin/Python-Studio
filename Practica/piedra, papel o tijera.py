import random
from colorama import Fore, Style, init


print(f"""
{Fore.MAGENTA}
██████╗░░█████╗░░█████╗░██╗░░██╗   ██████╗░░█████╗░██████╗░███████╗██████╗░   ░█████╗░██████╗░   ████████╗██████╗░░█████╗░░██████╗██╗░░██╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝   ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗   ██╔══██╗██╔══██╗   ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║░░██║██╔══██╗
██████╔╝██║░░██║██║░░╚═╝█████═╝░   ██████╔╝███████║██████╔╝█████╗░░██████╔╝   ██║░░██║██████╔╝   ░░░██║░░░██████╔╝███████║╚█████╗░███████║╚═╝███╔╝
██╔══██╗██║░░██║██║░░██╗██╔═██╗░   ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗   ██║░░██║██╔══██╗   ░░░██║░░░██╔══██╗██╔══██║░╚═══██╗██╔══██║░░░╚══╝░
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗   ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║   ╚█████╔╝██║░░██║   ░░░██║░░░██║░░██║██║░░██║██████╔╝██║░░██║░░░██╗░░
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝   ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝   ░╚════╝░╚═╝░░╚═╝   ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░
""""")

# Inicializar colorama
init(autoreset=True)

print(f"""
{Style.BRIGHT}{Fore.CYAN}Reglas del juego:
{Fore.YELLOW}- Piedra:
{Fore.GREEN}* Gana contra Tijera y Basura.
{Fore.RED}* Pierde contra Papel, Mechero y Agua.
{Fore.YELLOW}- Papel:
{Fore.GREEN}* Gana contra Piedra y Basura.
{Fore.RED}* Pierde contra Tijera y Agua.
{Fore.YELLOW}- Tijera:
{Fore.GREEN}* Gana contra Papel y Agua.
{Fore.RED}* Pierde contra Piedra y Mechero.
{Fore.YELLOW}- Basura:
{Fore.GREEN}* Gana contra Tijera.
{Fore.RED}* Pierde contra Piedra, Papel, Mechero y Agua.
{Fore.YELLOW}- Mechero:
{Fore.GREEN}* Gana contra Piedra, Tijera y Basura.
{Fore.RED}* Pierde contra Papel y Agua.
{Fore.YELLOW}- Agua:
{Fore.GREEN}* Gana contra Piedra, Papel, Basura y Mechero.
{Fore.RED}* Pierde contra Tijera.
""")

opciones = {
    1: "Piedra",
    2: "Papel",
    3: "Tijera",
    4: "Basura",
    5: "Mechero",
    6: "Agua"
}

while True:
    
    print(f"""{Fore.CYAN}
¿Qué eliges?
1. Piedra
2. Papel
3. Tijera
4. Basura
5. Mechero
6. Agua
  """)

    h_usuario = int(input(f"{Fore.YELLOW}Elije una opción: ")) 
    if h_usuario != 1 and h_usuario != 2 and h_usuario != 3 and h_usuario != 4 and h_usuario != 5 and h_usuario != 6:
        print(f"{Fore.RED}Opción no válida, elige entre 1 y 6")
        continue
    h_maquina = random.randint(1, 6)           

    print(f"{Fore.CYAN}El usuario ha elegido: {opciones[h_usuario]}")
    print(f"{Fore.CYAN}La máquina ha elegido: {opciones[h_maquina]}")

    if h_usuario == 1 and h_maquina == 1:   
        print(f"{Fore.LIGHTBLUE_EX}Empate")
    elif h_usuario == 2 and h_maquina == 1:
        print(f"{Fore.GREEN}Ganaste, papel envuelve piedra")
    elif h_usuario == 3 and h_maquina == 1:
        print(f"{Fore.RED}Perdiste, piedra rompe tijera")
    elif h_usuario == 4 and h_maquina == 1:
        print(f"{Fore.RED}Perdiste, piedra rompe basura")
    elif h_usuario == 5 and h_maquina == 1:
        print(f"{Fore.GREEN}Ganaste, mechero derrite piedra")
    elif h_usuario == 6 and h_maquina == 1:
        print(f"{Fore.GREEN}Ganaste, agua desgasta piedra")
    elif h_usuario == 1 and h_maquina == 2:
        print(f"{Fore.RED}Perdiste, papel envuelve piedra")
    elif h_usuario == 2 and h_maquina == 2:
        print(f"{Fore.LIGHTBLUE_EX}Empate")
    elif h_usuario == 3 and h_maquina == 2:
        print(f"{Fore.GREEN}Ganaste, tijera corta papel")
    elif h_usuario == 4 and h_maquina == 2:
        print(f"{Fore.RED}Perdiste, papel ensucia basura")
    elif h_usuario == 5 and h_maquina == 2:
        print(f"{Fore.RED}Perdiste, papel apaga mechero")
    elif h_usuario == 6 and h_maquina == 2:
        print(f"{Fore.GREEN}Ganaste, agua moja papel")
    elif h_usuario == 1 and h_maquina == 3:
        print(f"{Fore.GREEN}Ganaste, piedra rompe tijera")
    elif h_usuario == 2 and h_maquina == 3:
        print(f"{Fore.RED}Perdiste, tijera corta papel")
    elif h_usuario == 3 and h_maquina == 3:
        print(f"{Fore.LIGHTBLUE_EX}Empate")
    elif h_usuario == 4 and h_maquina == 3:
        print(f"{Fore.GREEN}Ganaste, basura bloquea tijera")
    elif h_usuario == 5 and h_maquina == 3:
        print(f"{Fore.GREEN}Ganaste, mechero derrite tijera")
    elif h_usuario == 6 and h_maquina == 3:
        print(f"{Fore.RED}Perdiste, tijera corta agua")
    elif h_usuario == 1 and h_maquina == 4:
        print(f"{Fore.GREEN}Ganaste, piedra rompe basura")
    elif h_usuario == 2 and h_maquina == 4:
        print(f"{Fore.GREEN}Ganaste, papel ensucia basura")
    elif h_usuario == 3 and h_maquina == 4:
        print(f"{Fore.RED}Perdiste, basura bloquea tijera")
    elif h_usuario == 4 and h_maquina == 4:
        print(f"{Fore.LIGHTBLUE_EX}Empate")
    elif h_usuario == 5 and h_maquina == 4:
        print(f"{Fore.GREEN}Ganaste, mechero quema basura")
    elif h_usuario == 6 and h_maquina == 4:
        print(f"{Fore.GREEN}Ganaste, agua limpia basura")
    elif h_usuario == 1 and h_maquina == 5:
        print(f"{Fore.RED}Perdiste, mechero derrite piedra")
    elif h_usuario == 2 and h_maquina == 5:
        print(f"{Fore.GREEN}Ganaste, papel apaga mechero")
    elif h_usuario == 3 and h_maquina == 5:
        print(f"{Fore.RED}Perdiste, mechero derrite tijera")
    elif h_usuario == 4 and h_maquina == 5:
        print(f"{Fore.RED}Perdiste, mechero quema basura")
    elif h_usuario == 5 and h_maquina == 5:
        print(f"{Fore.LIGHTBLUE_EX}Empate")
    elif h_usuario == 6 and h_maquina == 5:
       print(f"{Fore.GREEN}Ganaste, agua apaga mechero")
    elif h_usuario == 1 and h_maquina == 6:
        print(f"{Fore.RED}Perdiste, agua desgasta piedra")
    elif h_usuario == 2 and h_maquina == 6:
        print(f"{Fore.RED}Perdiste, agua moja papel")
    elif h_usuario == 3 and h_maquina == 6:
        print(f"{Fore.GREEN}Ganaste, tijera corta agua")
    elif h_usuario == 4 and h_maquina == 6:
        print(f"{Fore.RED}Perdiste, agua limpia basura")
    elif h_usuario == 5 and h_maquina == 6:
        print(f"{Fore.RED}Perdiste, agua apaga mechero")
    elif h_usuario == 6 and h_maquina == 6:
        print(f"{Fore.LIGHTBLUE_EX}Empate")
    else:
        print(f"{Fore.YELLOW}Opción no válida, elige entre 1 y 6")
    
    if input(f"{Fore.YELLOW}¿Quieres jugar otra vez? Si o No: ").lower() != 'si': 
        print(f"{Fore.YELLOW}Gracias por jugar") 
        break
    
print(f"{Fore.YELLOW}Fin del juego")
print(f"{Fore.YELLOW}¡Hasta la próxima!")