print(" ")
print("Alvarez Delgado Yael Ismael 3-W 1172, Ejercicio 6")
print(" ")
# Función para verificar si el email es válido
def es_email_valido(email):
    # Verificar si la dirección contiene al menos un "@" 
    if "@" in email:
        return True
    else:
        return False

# Solicitar al usuario que ingrese una dirección de email
email = input("Introduce una dirección de email: ")

# Llamar a la función para verificar si el email es válido
if es_email_valido(email):
    print("La dirección de email es válida.")
else:
    print("La dirección de email no es válida.")