import random # Importamos el modulo 'random'

def tirar_dado(): # Definimos una función que vamos a usar para el dado.
    n = random.randrange(1,6) # Llamamos a la función "randrange" perteneciente al modulo "random".
    return(n) # Retornamos el valor de n al alcance global en la invocación.


n1 = tirar_dado() # Invocamos la función "tirar dado" y guardamos el valor retornado.
n2 = tirar_dado() 
n3 = tirar_dado()

print("Lanzamiento 1:", n1)
print("Lanzamiento 2:", n2) 
print("Lanzamiento 3:", n3) 

sum = n1 + n2 + n3 # Sumamos todos los valores.
print("Suma total:", sum)
