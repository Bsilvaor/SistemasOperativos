import os
import threading

def imprimir_pid():
    pid = os.getpid()
    print(f"El PID del proceso es: {pid}")

if __name__ == "__main__":
    # Crea un hilo
    thread = threading.Thread(target=imprimir_pid)

    # Inicia el hilo
    thread.start()

    # Espera a que el hilo termine (opcional)
    thread.join()

    # El código a continuación seguirá ejecutándose en el hilo principal
