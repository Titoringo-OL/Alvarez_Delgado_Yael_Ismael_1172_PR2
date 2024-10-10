print(" ")
print("Alvarez Delgado Yael Ismael 3-W 1172, Ejercicio 11")
print(" ")
# Función que calcula la distancia dirigida entre dos puntos en un plano cartesiano.
def distancia_dirigida(punto1, punto2):

    # Desempaquetamos las coordenadas de los puntos
    x1, y1 = punto1
    x2, y2 = punto2

    # Calculamos la distancia dirigida
    distancia = ((x2 - x1), (y2 - y1))  # Diferencias en x e y
    return distancia

# Ejemplo de uso
punto_a = (3, 4)  # Primer punto (x1, y1)
punto_b = (7, 1)  # Segundo punto (x2, y2)

# Llamamos a la función y mostramos el resultado
resultado = distancia_dirigida(punto_a, punto_b)
print(f"La distancia dirigida entre los puntos {punto_a} y {punto_b} es: {resultado}")  # Salida: (4, -3)
