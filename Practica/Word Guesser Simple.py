import random
import colorama
from colorama import Fore, Style, init
import tkinter as tk

colorama.init()

word_bank = [
    'abaco', 'abada', 'abajo', 'abeja', 'abeto', 'abril', 'abrir', 'actor',
    'aereo', 'aforo', 'ahora', 'ajuar', 'alelo', 'alfar', 'alfoz', 'altar',
    'amigo', 'andar', 'arbol', 'arena', 'argon', 'arido', 'arnes', 'arroz',
    'astro', 'atajo', 'avion', 'avena', 'ayuda', 'azote', 'babel', 'babor',
    'bagre', 'bahia', 'baile', 'banal', 'barco', 'barba', 'basar', 'basto',
    'batir', 'becas', 'beber', 'bella', 'belen', 'belga', 'besos', 'bocas',
    'bolsa', 'bolso', 'bonito', 'borra', 'botas', 'boxeo', 'brisa', 'bravo',
    'broma', 'bruno', 'burro', 'campo', 'canto', 'carta', 'casco', 'caspa',
    'casta', 'cazar', 'ceder', 'celda', 'censo', 'cerdo', 'certe', 'cielo',
    'circo', 'clara', 'claro', 'clave', 'clima', 'cobre', 'cobra', 'colmo',
    'color', 'corte', 'costa', 'criar', 'crudo', 'cuadro', 'cuerda', 'cuento',
    'curar', 'dado', 'deber', 'decir', 'dedos', 'denso', 'deseo', 'diario',
    'dicha', 'diente', 'digna', 'diosa', 'dista', 'doble', 'dolor', 'domar',
    'donde', 'dulce', 'duelo', 'dueno', 'echar', 'eleva', 'ellos', 'embar',
    'epoca', 'equipo', 'error', 'escala', 'espia', 'estar', 'estos', 'etapa',
    'etico', 'evita', 'exito', 'falta', 'falso', 'favor', 'feliz', 'fibra',
    'fiera', 'firma', 'firme', 'flora', 'flaco', 'flama', 'flota', 'focar',
    'fogon', 'forma', 'frase', 'freir', 'fuego', 'fuera', 'gente', 'globo',
    'gordo', 'grave', 'grato', 'grito', 'grupo', 'guapo', 'haber', 'hacia',
    'harto', 'hielo', 'hija', 'hilar', 'hombre', 'honor', 'hondo', 'hotel',
    'humor', 'ideal', 'igual', 'imagen', 'impar', 'inicio', 'inmune', 'inutil',
    'iria', 'joven', 'joyas', 'jugar', 'junto', 'justo', 'labio', 'largo',
    'latas', 'laudo', 'leche', 'lecho', 'legar', 'lejia', 'lejos', 'lento',
    'lena', 'leon', 'letra', 'lidia', 'linda', 'lista', 'llama', 'llave',
    'lleno', 'llorar', 'locale', 'lomas', 'lucha', 'lunar', 'luzco', 'magia',
    'maiz', 'malva', 'malla', 'mambo', 'marco', 'marea', 'mater', 'mayor',
    'mecha', 'media', 'mejor', 'meson', 'miedo', 'miles', 'mina', 'minar',
    'mirar', 'mismo', 'mitad', 'mango', 'nieve', 'pasta', 'pinta', 'plato',
    'pluma', 'polvo', 'pueda', 'ruido', 'salon', 'sello', 'silla', 'surco',
    'tarde', 'tigre', 'tomas', 'tarea', 'tiros', 'usado', 'vasta', 'vocal',
    'yacer', 'zorro', 'amado', 'barco', 'calma', 'diana', 'fondo', 'gallo',
    'hielo', 'india', 'juego', 'karma', 'lento', 'manos', 'nadar', 'ovino',
    'piano', 'quien', 'raton', 'salud', 'tonto', 'urban', 'valle', 'zona',
    'bella', 'bueno', 'claro', 'dulce', 'fuego', 'grato', 'heroe', 'ideal',
    'joven', 'libro', 'miedo', 'nuevo', 'plaza', 'quiza', 'robar', 'sabor',
    'tabla', 'union', 'visto', 'zapato'
]

# Eleccion de palabra / itentos.
word = random.choice(word_bank)
attempts = len(word)


# Se rellena la variable resultado con guión bajo (luego los guiones seran sustituidos por las letras correctas).
result = ['_'] * len(word)

print(result)

# Iniciamos proceso de adivinar la palbra.
while attempts > 0:
    attempts -= 1
    userword = str(input("Cual es la palabra? "))
    if len(userword) != len(word):
        print("Tamaño incorrecto")
        attempts += 1
        continue

    # Condición ganadora
    if userword == word: 
        print(f"{Fore.LIGHTCYAN_EX}Enhorabuena, has encontrado la palabra: " + f"{Fore.LIGHTGREEN_EX}{word}" + ".")
        break
    
    # Iniciamos bucle para sustituir los guiones de "result" por las letras si son correctas.
    for i in range(len(userword)):
        if userword[i] == word[i]:
            result[i] = (f"{Fore.GREEN}{userword[i]}{Style.RESET_ALL}")
    

    # Iniciamos bucle para sustituir los guiones de "result" por las letras si son incorrectas.
    for i in range(len(userword)):
        if userword[i] != word[i] and userword[i] not in word:  # Si la letra no está en la palabra
            result[i] = (f"{Fore.RED}{userword[i]}{Style.RESET_ALL}")
            
        # Iniciamos bucle para sustituir los guiones de "result" por las letras si no estan en la posición correcta.
    for i in range(len(userword)):
        if userword[i] != word[i] and userword[i] in word:  # Si la letra no está en la palabra
            result[i] = (f"{Fore.YELLOW}{userword[i]}{Style.RESET_ALL}")
            
    print("".join(result))

if attempts == 0:
    print(f"{Fore.LIGHTMAGENTA_EX}Se te han acabado los intentos, vuelve a intentarlo.")
    print(f"{Fore.LIGHTMAGENTA_EX}Tu palbra es: " + f"{Fore.LIGHTMAGENTA_EX}{word}" + ".")


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


