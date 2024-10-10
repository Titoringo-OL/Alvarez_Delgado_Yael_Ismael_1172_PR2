# 1- Funcion que muestre el saludo Hey amigos! cada vez que se le pida
# Alvarez Delgado Yael Ismael 3-W
def mostrar_saludo():
    """Función que imprime un saludo."""
    print("Hey amigos!")
print(" ")
# Bucle que se ejecuta indefinidamente hasta que el usuario decida salir
while True:
    # Solicita al usuario que ingrese un comando
    pedido = input("Escribe 'hola' para recibir un saludo o 'salir' para terminar: ").strip().lower()
    
    # Verifica si el usuario quiere recibir un saludo
    if pedido == 'hola':
        mostrar_saludo()  # Llama a la función para mostrar el saludo
        print(" ")
    # Verifica si el usuario quiere salir
    elif pedido == 'salir':
        print("¡Hasta luego!")  # Mensaje de despedida
        break  # Sale del bucle
    else:
        # Mensaje en caso de que el comando no sea reconocido
        print("Comando no reconocido. Por favor, escribe 'saludo' o 'salir'.")
