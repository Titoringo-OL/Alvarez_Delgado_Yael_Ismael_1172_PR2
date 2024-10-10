print(" ")
print("Alvarez Delgado Yael Ismael 3-W 1172, Ejercicio 4")
print(" ")
import math
# Definición de la función para calcular el total de la factura con IVA
def calcular_total_factura(cantidad_sin_iva, porcentaje_iva_por_defecto=21):
    iva = (porcentaje_iva_por_defecto / 100) * cantidad_sin_iva
    total_factura = cantidad_sin_iva + iva
    return total_factura

# Solicitar al usuario la cantidad sin IVA
cantidad_sin_iva = float(input("Introduce la cantidad sin IVA: "))

# Solicitar al usuario el porcentaje de IVA a aplicar, si no se introduce, se aplicará 21%
porcentaje_iva_del_usuario = input("Introduce el porcentaje de IVA (presiona Enter para usar 21%): ")

# Verificar si el usuario ingresó un porcentaje de IVA
if porcentaje_iva_del_usuario:
    porcentaje_iva = float(porcentaje_iva_del_usuario)
else:
    porcentaje_iva = 21  # Valor por defecto

# Calcular el total de la factura
total = calcular_total_factura(cantidad_sin_iva, porcentaje_iva)

# Mostrar el total de la factura
print(f"El total de la factura con IVA es: {total:.2f}")