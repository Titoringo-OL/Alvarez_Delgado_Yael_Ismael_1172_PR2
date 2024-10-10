print(" ")
print("Alvarez Delgado Yael Ismael 3-W 1172, Ejercicio 7")
print(" ")
def longitud_ultima_palabra(s):
    # Eliminar espacios al principio y al final, y dividir por espacios
    palabras = s.strip().split()
    
    # Verificar si hay palabras y devolver la longitud de la última
    if palabras:
        return len(palabras[-1])
    return 0

# Ejemplo de uso
texto = "   Hola    mundo   "
print(longitud_ultima_palabra(texto))  # Salida: 5
