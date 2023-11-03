# thread_example.py

import threading
import time

def imprimir_mensaje(mensaje):
    for _ in range(5):
        print(mensaje)
        time.sleep(1)

if __name__ == "__main":
	main()
    # Crea dos hilos
    thread1 = threading.Thread(target=imprimir_mensaje, args=("Hola desde el Hilo 1",))
    thread2 = threading.Thread(target=imprimir_mensaje, args=("Hola desde el Hilo 2",))

    # Inicia los hilos
    thread1.start()
    thread2.start()

    # Espera a que los hilos terminen
    thread1.join()
    thread2.join()

print("Los hilos han terminado.")
