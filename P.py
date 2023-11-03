# multiprocessing_example.py

# Importa el módulo multiprocessing, que proporciona funcionalidad para trabajar con procesos.
import multiprocessing, threading


# Importa el módulo time, que se utilizará para agregar retrasos en el programa.
import time

# Define una función llamada imprimir_mensaje que acepta un argumento mensaje.
def imprimir_mensaje(mensaje):
    #Accedo a la variable global definida más abajo en el MAIN.
    global a
    a = a + 1
    print(a)
# Define una función principal llamada main, que contendrá el código principal del programa.
def main():
    # Crea dos procesos: proceso1 y proceso2, que ejecutarán la función imprimir_mensaje con diferentes mensajes.
    proceso1 = multiprocessing.Process(target=imprimir_mensaje, args=("Hola desde el Proceso 1",))
    proceso2 = multiprocessing.Process(target=imprimir_mensaje, args=("Hola desde el Proceso 2",))
    # Creo dos hilos para ver la diferencia entre procesos y los hilos.
    thread1 = threading.thread(target=imprimir_mensaje, args=("Hola desde el Hilo 1",))
    thread2 = threading.Thread(target=imprimir_mensaje, args=("Hola desde el Hilo 2",))
    # Inicia los procesos, lo que comienza la ejecución de la función imprimir_mensaje en cada proceso.
    proceso1.start()
    proceso2.start()
    # Una vez creados los hilos iniciamos los procesos de estos:
    thread1.start()
    thread2.start()
    # Espera a que los procesos terminen antes de continuar con el código principal.
    proceso1.join()
    proceso2.join()
    # Espero a que los hilos terminen antes de continuar el código principal.
    thread1.join()
    thread2.join()
    # Imprime un mensaje indicando que los procesos han terminado.
    print("Los procesos han terminado.")

# Verifica si este script se está ejecutando como el programa principal.
if __name__ == "__main__":
    a = 10   
    # Llama a la función main para iniciar el programa.
    main()
