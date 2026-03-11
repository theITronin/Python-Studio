import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

print(f"""
{Fore.MAGENTA}
██████╗░░█████╗░░█████╗░██╗░░██╗   ██████╗░░█████╗░██████╗░███████╗██████╗░   ░█████╗░██████╗░   ████████╗██████╗░░█████╗░░██████╗██╗░░██╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝   ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗   ██╔══██╗██╔══██╗   ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║░░██║██╔══██╗
██████╔╝██║░░██║██║░░╚═╝█████═╝░   ██████╔╝███████║██████╔╝█████╗░░██████╔╝   ██║░░██║██████╔╝   ░░░██║░░░██████╔╝███████║╚█████╗░███████║╚═╝███╔╝
██╔══██╗██║░░██║██║░░██╗██╔═██╗░   ██╔═══╝░██╔══██╗██╔═══╝░██╔══╝░░██╔══██╗   ██║░░██║██╔══██╗   ░░░██║░░░██╔══██╗██╔══██║░╚═══██╗██╔══██║░░░╚══╝░
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗   ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║   ╚█████╔╝██║░░██║   ░░░██║░░░██║░░██║██║░░██║██████╔╝██║░░██║░░░██╗░░
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝   ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝   ░╚════╝░╚═╝░░╚═╝   ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░
""""")

print(f"""
{Style.BRIGHT}{Fore.CYAN}Game Rules:
{Fore.YELLOW}- Rock:
{Fore.GREEN}* Wins against Scissors and Trash.
{Fore.RED}* Loses against Paper, Lighter, and Water.
{Fore.YELLOW}- Paper:
{Fore.GREEN}* Wins against Rock and Trash.
{Fore.RED}* Loses against Scissors and Water.
{Fore.YELLOW}- Scissors:
{Fore.GREEN}* Wins against Paper and Water.
{Fore.RED}* Loses against Rock and Lighter.
{Fore.YELLOW}- Trash:
{Fore.GREEN}* Wins against Scissors.
{Fore.RED}* Loses against Rock, Paper, Lighter, and Water.
{Fore.YELLOW}- Lighter:
{Fore.GREEN}* Wins against Rock, Scissors, and Trash.
{Fore.RED}* Loses against Paper and Water.
{Fore.YELLOW}- Water:
{Fore.GREEN}* Wins against Rock, Paper, Trash, and Lighter.
{Fore.RED}* Loses against Scissors.
""")

options = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
    4: "Trash",
    5: "Lighter",
    6: "Water"
}

while True:
    
    print(f"""{Fore.CYAN}
What do you choose?
1. Rock
2. Paper
3. Scissors
4. Trash
5. Lighter
6. Water
  """)

    user_choice = int(input(f"{Fore.YELLOW}Choose an option: ")) 
    if user_choice not in range(1, 7):
        print(f"{Fore.RED}Invalid option, please choose between 1 and 6")
        continue
    
    computer_choice = random.randint(1, 6)           

    print(f"{Fore.CYAN}User chose: {options[user_choice]}")
    print(f"{Fore.CYAN}Computer chose: {options[computer_choice]}")

    if user_choice == 1 and computer_choice == 1:   
        print(f"{Fore.LIGHTBLUE_EX}Tie")
    elif user_choice == 2 and computer_choice == 1:
        print(f"{Fore.GREEN}You win, paper covers rock")
    elif user_choice == 3 and computer_choice == 1:
        print(f"{Fore.RED}You lose, rock breaks scissors")
    elif user_choice == 4 and computer_choice == 1:
        print(f"{Fore.RED}You lose, rock breaks trash")
    elif user_choice == 5 and computer_choice == 1:
        print(f"{Fore.GREEN}You win, lighter melts rock")
    elif user_choice == 6 and computer_choice == 1:
        print(f"{Fore.GREEN}You win, water wears down rock")
    elif user_choice == 1 and computer_choice == 2:
        print(f"{Fore.RED}You lose, paper covers rock")
    elif user_choice == 2 and computer_choice == 2:
        print(f"{Fore.LIGHTBLUE_EX}Tie")
    elif user_choice == 3 and computer_choice == 2:
        print(f"{Fore.GREEN}You win, scissors cut paper")
    elif user_choice == 4 and computer_choice == 2:
        print(f"{Fore.RED}You lose, paper dirties trash")
    elif user_choice == 5 and computer_choice == 2:
        print(f"{Fore.RED}You lose, paper smothers lighter")
    elif user_choice == 6 and computer_choice == 2:
        print(f"{Fore.GREEN}You win, water soaks paper")
    elif user_choice == 1 and computer_choice == 3:
        print(f"{Fore.GREEN}You win, rock breaks scissors")
    elif user_choice == 2 and computer_choice == 3:
        print(f"{Fore.RED}You lose, scissors cut paper")
    elif user_choice == 3 and computer_choice == 3:
        print(f"{Fore.LIGHTBLUE_EX}Tie")
    elif user_choice == 4 and computer_choice == 3:
        print(f"{Fore.GREEN}You win, trash blocks scissors")
    elif user_choice == 5 and computer_choice == 3:
        print(f"{Fore.GREEN}You win, lighter melts scissors")
    elif user_choice == 6 and computer_choice == 3:
        print(f"{Fore.RED}You lose, scissors cut water")
    elif user_choice == 1 and computer_choice == 4:
        print(f"{Fore.GREEN}You win, rock breaks trash")
    elif user_choice == 2 and computer_choice == 4:
        print(f"{Fore.GREEN}You win, paper dirties trash")
    elif user_choice == 3 and computer_choice == 4:
        print(f"{Fore.RED}You lose, trash blocks scissors")
    elif user_choice == 4 and computer_choice == 4:
        print(f"{Fore.LIGHTBLUE_EX}Tie")
    elif user_choice == 5 and computer_choice == 4:
        print(f"{Fore.GREEN}You win, lighter burns trash")
    elif user_choice == 6 and computer_choice == 4:
        print(f"{Fore.GREEN}You win, water cleans trash")
    elif user_choice == 1 and computer_choice == 5:
        print(f"{Fore.RED}You lose, lighter melts rock")
    elif user_choice == 2 and computer_choice == 5:
        print(f"{Fore.GREEN}You win, paper smothers lighter")
    elif user_choice == 3 and computer_choice == 5:
        print(f"{Fore.RED}You lose, lighter melts scissors")
    elif user_choice == 4 and computer_choice == 5:
        print(f"{Fore.RED}You lose, lighter burns trash")
    elif user_choice == 5 and computer_choice == 5:
        print(f"{Fore.LIGHTBLUE_EX}Tie")
    elif user_choice == 6 and computer_choice == 5:
       print(f"{Fore.GREEN}You win, water puts out lighter")
    elif user_choice == 1 and computer_choice == 6:
        print(f"{Fore.RED}You lose, water wears down rock")
    elif user_choice == 2 and computer_choice == 6:
        print(f"{Fore.RED}You lose, water soaks paper")
    elif user_choice == 3 and computer_choice == 6:
        print(f"{Fore.GREEN}You win, scissors cut water")
    elif user_choice == 4 and computer_choice == 6:
        print(f"{Fore.RED}You lose, water cleans trash")
    elif user_choice == 5 and computer_choice == 6:
        print(f"{Fore.RED}You lose, water puts out lighter")
    elif user_choice == 6 and computer_choice == 6:
        print(f"{Fore.LIGHTBLUE_EX}Tie")
    else:
        print(f"{Fore.YELLOW}Invalid option, please choose between 1 and 6")
    
    if input(f"{Fore.YELLOW}Do you want to play again? Yes or No: ").lower() not in ['yes', 'y', 'si']: 
        print(f"{Fore.YELLOW}Thanks for playing!") 
        break
    
print(f"{Fore.YELLOW}Game Over")
print(f"{Fore.YELLOW}See you next time!")