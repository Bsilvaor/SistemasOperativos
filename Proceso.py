import os
import multiprocessing

def imprimir_pid():
    pid = os.getpid()
    print(f"El PID del proceso es: {pid}")

if __name__ == "__main__":
    # Crea un proceso
    proceso = multiprocessing.Process(target=imprimir_pid)

    # Inicia el proceso
    proceso.start()

    # Espera a que el proceso termine (opcional)
    proceso.join()

    # El código a continuación seguirá ejecutándose en el proceso principal
