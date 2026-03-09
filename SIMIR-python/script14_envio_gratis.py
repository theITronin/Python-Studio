
# Declaramos variable importe y le ingresamos el valor de la entrada validada como float.
importe = float(input("Cuál fue el importe de la compra (€): "))

# Condiciones:
if importe < 0: # Validamos que el importe no sea negativo
    print("Importe invalido.")
elif importe >= 50: # Importe mayor o igual qué 50
    print("Envio gratis.")
    print(f"Total: {importe}")
else:
    costo_envio = 4.99 # otra variable útil
    total = importe + costo_envio
    print("El envío cuesta 4,99€.") # Importe menor a 50
    print(f"Envío: {costo_envio} €. Total {total} €") # Imprimimos el total (importe más )
