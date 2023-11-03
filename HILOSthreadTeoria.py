# thread_example.py

# Importa el módulo threading, que proporciona funcionalidad para trabajar con hilos.
import threading

# Importa el módulo time, que se utilizará para agregar retrasos en el programa.
import time

# Define una función llamada imprimir_mensaje que acepta un argumento mensaje.
def imprimir_mensaje(mensaje):
    # Inicia un bucle for que se ejecutará cinco veces.
    for _ in range(5):
        # Imprime el mensaje recibido como argumento.
        print(mensaje)
        # Agrega un retraso de 1 segundo antes de la siguiente iteración.
        time.sleep(1)

# Define una función principal llamada main, que contendrá el código principal del programa.
def main():
    # Crea dos hilos: thread1 y thread2, que ejecutarán la función imprimir_mensaje con diferentes mensajes.
    thread1 = threading.Thread(target=imprimir_mensaje, args=("Hola desde el Hilo 1",))
    thread2 = threading.Thread(target=imprimir_mensaje, args=("Hola desde el Hilo 2",))

    # Inicia los hilos, lo que comienza la ejecución de la función imprimir_mensaje en cada hilo.
    thread1.start()
    thread2.start()

    # Espera a que los hilos terminen antes de continuar con el código principal.
    thread1.join()
    thread2.join()

    # Imprime un mensaje indicando que los hilos han terminado.
    print("Los hilos han terminado.")

# Verifica si este script se está ejecutando como el programa principal.
if __name__ == "__main__":
    # Llama a la función main para iniciar el programa.
    main()
