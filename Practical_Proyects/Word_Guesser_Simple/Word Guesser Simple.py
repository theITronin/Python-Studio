import random
import colorama
from colorama import Fore, Style, init
import tkinter as tk

colorama.init()

# Word bank translated to English (5-letter words)
word_bank = [
    'apple', 'beach', 'brain', 'bread', 'brush', 'chair', 'chest', 'chord',
    'click', 'clock', 'cloud', 'dance', 'diary', 'drink', 'earth', 'flame',
    'floor', 'fruit', 'glass', 'grape', 'green', 'heart', 'house', 'juice',
    'light', 'lemon', 'money', 'music', 'night', 'ocean', 'paint', 'paper',
    'phone', 'piano', 'plant', 'radio', 'river', 'scene', 'shirt', 'sleep',
    'small', 'smile', 'snake', 'space', 'spoon', 'storm', 'table', 'tiger',
    'toast', 'touch', 'train', 'truck', 'voice', 'water', 'watch', 'whale',
    'world', 'write', 'youth', 'zebra', 'above', 'actor', 'adult', 'alive',
    'alone', 'angry', 'areas', 'aside', 'asked', 'avoid', 'awful', 'backy',
    'basic', 'basis', 'begin', 'below', 'birth', 'black', 'blind', 'block',
    'blood', 'board', 'bonus', 'books', 'bound', 'break', 'brief', 'build',
    'built', 'buyer', 'cable', 'calmly', 'carry', 'cases', 'cause', 'chain',
    'check', 'china', 'chose', 'civil', 'claim', 'class', 'clean', 'clear',
    'climb', 'close', 'coach', 'coast', 'count', 'court', 'cover', 'craft',
    'crash', 'cream', 'crime', 'cross', 'crowd', 'crown', 'curve', 'cycle',
    'daily', 'dated', 'death', 'depth', 'doubt', 'draft', 'drama', 'drawn',
    'dream', 'dress', 'drive', 'drove', 'dying', 'eager', 'early', 'earth',
    'eight', 'elite', 'empty', 'enemy', 'enjoy', 'enter', 'error', 'event'
]

# Word selection / attempts
word = random.choice(word_bank)
attempts = len(word)

# The result variable is filled with underscores (later replaced by correct letters)
result = ['_'] * len(word)

print(result)

# Start the process of guessing the word
while attempts > 0:
    attempts -= 1
    user_word = str(input("What is the word? "))
    
    if len(user_word) != len(word):
        print("Incorrect size")
        attempts += 1
        continue

    # Winning condition
    if user_word == word: 
        print(f"{Fore.LIGHTCYAN_EX}Congratulations, you found the word: " + f"{Fore.LIGHTGREEN_EX}{word}" + ".")
        break
    
    # Loop to replace underscores in "result" with letters if they are in the correct position (Green)
    for i in range(len(user_word)):
        if user_word[i] == word[i]:
            result[i] = (f"{Fore.GREEN}{user_word[i]}{Style.RESET_ALL}")
    
    # Loop to replace underscores in "result" if the letter is NOT in the word (Red)
    for i in range(len(user_word)):
        if user_word[i] != word[i] and user_word[i] not in word:
            result[i] = (f"{Fore.RED}{user_word[i]}{Style.RESET_ALL}")
            
    # Loop to replace underscores in "result" if the letter is in the word but WRONG position (Yellow)
    for i in range(len(user_word)):
        if user_word[i] != word[i] and user_word[i] in word:
            result[i] = (f"{Fore.YELLOW}{user_word[i]}{Style.RESET_ALL}")
            
    print("".join(result))

if attempts == 0 and user_word != word:
    print(f"{Fore.LIGHTMAGENTA_EX}You have run out of attempts, try again.")
    print(f"{Fore.LIGHTMAGENTA_EX}The word was: " + f"{Fore.LIGHTMAGENTA_EX}{word}" + ".")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
