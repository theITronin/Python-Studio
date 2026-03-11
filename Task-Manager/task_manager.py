from colorama import Fore, Style, init
import json
import os
import tkinter as tk

print("""
░██████╗░███████╗░██████╗████████╗░█████╗░██████╗░  ██████╗░███████╗  ████████╗░█████╗░██████╗░███████╗░█████╗░░██████╗
██╔════╝░██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██╔════╝  ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝
██║░░██╗░█████╗░░╚█████╗░░░░██║░░░██║░░██║██████╔╝  ██║░░██║█████╗░░  ░░░██║░░░███████║██████╔╝█████╗░░███████║╚█████╗░
██║░░╚██╗██╔══╝░░░╚═══██╗░░░██║░░░██║░░██║██╔══██╗  ██║░░██║██╔══╝░░  ░░░██║░░░██╔══██║██╔══██╗██╔══╝░░██╔══██║░╚═══██╗
╚██████╔╝███████╗██████╔╝░░░██║░░░╚█████╔╝██║░░██║  ██████╔╝███████╗  ░░░██║░░░██║░░██║██║░░██║███████╗██║░░██║██████╔╝
░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝  ░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░
""")

init(autoreset=True)

directorio_actual = os.path.dirname(os.path.abspath(__file__))
archivo_tareas = os.path.join(directorio_actual, "tareas.json")

lista = []
tareas = {}

def cargar_tareas():
    try:
        with open(archivo_tareas, "r") as archivo: 
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open(archivo_tareas, "w") as archivo:
        json.dump(tareas, archivo, indent=4)
        


def añadir_tareas():
    lista = cargar_tareas()
    nombre = str(input("Cual es el nombre de la tarea: "))
    descripción = str(input("Cual es la descripción de la tarea: "))
    fecha_limite = str(input("Cual es la fecha limite de esta tarea -> ( xx:xx:xx ):"))
    estado = "Pendiente"
    tarea = [nombre, descripción, fecha_limite, estado]
    print(f"Se ha añadido esta nueva {tarea}: ")
    lista.append(tarea)
    guardar_tareas(lista)
    return lista

def eliminar_tareas():
    lista = cargar_tareas()
    nombre = str(input("Cual es el nombre de la tarea que deseas eliminar: "))
    for i in lista:
        if i[0] == nombre:
            lista.remove(i)
            guardar_tareas(lista)
            print(f"Se ha eliminado la tarea {i}")
            break
def modificar_tarea():
    lista = cargar_tareas()
    nombre =  str(input("Cual es el nombre de la tarea que deseas modificar: "))
    for i in lista:
        if i[0] == nombre:
            print("""
                1.Modificar nombre
                2.Modificar descripción
                3.Modificar fecha limite
                4.Modificar estado  
                  """)
            modif = int(input("Que deseas modificar: "))
            if modif == 1:
                nombre = str(input("Cual es el nuevo nombre de la tarea: "))
                i[0] = nombre
                
            if modif == 2:
                descripción = str(input("Cual es la nueva descripción de la tarea: "))
                i[1] = descripción
                
            if modif == 3:
                fecha_limite = str(input("Cual es la nueva fecha limite de esta tarea -> ( xx:xx:xx ):"))
                i[2] = fecha_limite
                
            if modif == 4:
                print("""
                     -Pendiente
                     -En progreso  
                     -Finalizada
                       """)
                estado = str(input("Cual es el nuevo estado de la tarea: "))
                i[3] = estado 
            guardar_tareas(lista)
                
            
    
while True:
    print(
"""
1.Añadir tareas
2.Eliminar tareas
3.Modificar tareas
"""
)
    
    
    opción = int(input("Que opción prefieres: "))
    if opción == 1:
        añadir_tareas()
    if opción == 2:
        eliminar_tareas()
    if opción == 3:
        modificar_tarea()
        
    print(       
f"""{Fore.LIGHTCYAN_EX}

1.Continuar
2.Salir
3.Ver tareas

""")
    
    opcion_continuar = int(input("Elije un número para continuar: "))
    if opcion_continuar == 1:
        continue
    elif opcion_continuar == 2:
        break
    elif opcion_continuar == 3:
        lista = cargar_tareas()
        print(f"{Fore.LIGHTCYAN_EX}Estas son tus tareas: ")
        for tarea in lista:
            print(f"{Fore.LIGHTYELLOW_EX}{tarea[0]} - {tarea[1]} - {tarea[2]} - {tarea[3]}")
        print("""
            1.Continuar
            2.Salir   
            """)
        opcion_continuar = int(input("Elije un número para continuar: "))
        if opcion_continuar == 1:
            continue
        elif opcion_continuar == 2:
            break
    
for elemento in lista:
    print(f"{Fore.LIGHTCYAN_EX}Estas son tus tareas: ")
    print(f"{Fore.LIGHTYELLOW_EX}Tareas: {elemento}")
    