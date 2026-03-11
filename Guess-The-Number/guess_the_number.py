import random # Import modules
from colorama import Fore, Style, init

print(f"""
 {Fore.MAGENTA}     
▄██████░██░░░██░▄█████░▄██████░▄██████░░░████████░██░░░██░▄█████░░░██████▄░██░░░██░▄██▄▄██▄░█████▄░▄█████░█████▄
██░░░░░░██░░░██░██░░░░░██░░░░░░██░░░░░░░░░░░██░░░░██░░░██░██░░░░░░░██░░░██░██░░░██░██░██░██░██░░██░██░░░░░██░░██
██░░███░██░░░██░█████░░▀█████▄░▀█████▄░░░░░░██░░░░███████░█████░░░░██░░░██░██░░░██░██░██░██░█████░░█████░░█████▀
██░░░██░██░░░██░██░░░░░░░░░░██░░░░░░██░░░░░░██░░░░██░░░██░██░░░░░░░██░░░██░██░░░██░██░██░██░██░░██░██░░░░░██░░██
▀█████▀░▀█████▀░▀█████░██████▀░██████▀░░░░░░██░░░░██░░░██░▀█████░░░██░░░██░▀█████▀░██░██░██░█████▀░▀█████░██░░██
      """)
init(autoreset=True) # We define autoreset for colorama strings

while True: # We start the main while True loop 
    rNumber = random.randint(1, 10) # The random module choose a number.
    while True: # while True loop for user number.
        user_number = int(input(f"{Fore.LIGHTBLUE_EX}Guess the number between 1 to 10: ")) # Request user number.

        if user_number < 1 or user_number > 10 or str(user_number): # We validate the user's input.
            print(f"{Fore.LIGHTCYAN_EX}Number out of range. The number must be between 1 to 10.")
            continue
        else:
            break
    if rNumber == user_number: # We compare the random number with the user number
        print(f"{Fore.LIGHTCYAN_EX}You win!")
    else:
        print(f"{Fore.LIGHTCYAN_EX}You lose! Te number it was:", rNumber)
        
    if str(input(f"{Fore.LIGHTBLUE_EX}Do you want yo play again? yes or no: ").lower()) != 'yes':
        print(f"{Fore.LIGHTBLUE_EX}Gracias por jugar!")
        break
    
   
        
