print(" ")
print("Alvarez Delgado Yael Ismael 3-W 1172, Ejercicio 9")
print(" ")
# Función que suma todos los números de una lista.
def suma(lista):
    return sum(lista)

def multip(lista):
    
    resultado = 1  # Inicializamos el resultado en 1 (neutro para la multiplicación)
    for num in lista:
        resultado *= num  # Multiplicamos cada número en la lista al resultado
    return resultado

# Ejemplo de uso
numeros = [1, 2, 3, 4]

# Calculamos la suma y la multiplicación
resultado_suma = suma(numeros)
resultado_multiplicacion = multip(numeros)

# Imprimimos los resultados
print(f"Suma: {resultado_suma}")  # Salida: Suma: 10
print(f"Multiplicación: {resultado_multiplicacion}")  # Salida: Multiplicación: 24
