print(" ")
print("Alvarez Delgado Yael Ismael 3-W 1172, Ejercicio 10")
print(" ")
# Función que verifica si un carácter es una vocal.
def es_vocal(caracter):

    # Convertimos el carácter a minúsculas para facilitar la comparación
    caracter = caracter.lower()

    # Comprobamos si el carácter es una vocal
    if caracter in 'aeiou':
        return True  # Es una vocal
    else:
        return False  # No es una vocal

# Ejemplo de uso
caracter_a_probar = 'e'

# Llamamos a la función y mostramos el resultado
resultado = es_vocal(caracter_a_probar)
print(f"¿El carácter '{caracter_a_probar}' es una vocal? {resultado}")  # Salida: True
