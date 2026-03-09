import random 
import string

def generador_contraseña():
    
    diccionario = string.ascii_letters + string.digits + string.punctuation
    c = random.choice(diccionario)
    return(c) 

c1 = generador_contraseña()
c2 = generador_contraseña() 
c3 = generador_contraseña()
c4 = generador_contraseña()
c5 = generador_contraseña()
c6 = generador_contraseña()
c7 = generador_contraseña()
c8 = generador_contraseña()

passwd = c1 + c2 + c3 + c4 + c5 + c6 + c7 +c8 # Sumamos todos los valores.

print("La password:", passwd)
