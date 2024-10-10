print(" ")
print("Alvarez Delgado Yael Ismael 3-W 1172, Ejercicio 5")
print(" ")
import math
# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area
# Función para calcular el volumen de una esfera
def calcular_volumen_esfera(radio):
    volumen = (4/3) * math.pi * radio ** 3
    return volumen
# Funcion para calculr el volumen de un cilindro
def calcular_volumen_cilindro(radio, h):
    vol = math.pi * radio ** 2 * h
    return vol
# Solicitar el radio al usuario
radio = float(input("Introduce el radio: "))
h = float(input("Introduce la altura del cilindro: "))
# Calcular el área del círculo y el volumen de la esfera
area_circulo = calcular_area_circulo(radio)
volumen_esfera = calcular_volumen_esfera(radio)
volumen_cilindro = calcular_volumen_cilindro(radio, h)
# Mostrar los resultados
print(" ")
print(f"El área del círculo con radio {radio} es: {area_circulo:.2f}")
print(f"El volumen de la esfera con radio {radio} es: {volumen_esfera:.2f}")
print(f"El volumen de un cilindro con radio de {radio} y altura de {h} es: {volumen_cilindro:.2f}")