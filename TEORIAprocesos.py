# multiprocessing_example.py

# Importa el módulo multiprocessing, que proporciona funcionalidad para trabajar con procesos.
import multiprocessing

# Importa el módulo time, que se utilizará para agregar retrasos en el programa.
import time

# Define una función llamada imprimir_mensaje que acepta un argumento mensaje.
def imprimir_mensaje(mensaje):
     # LLamo a la variable global definida más abajo en el MAIN.
     global a
     # Inicia un bucle for que se ejecutará cinco veces.
     for _ in range(5):
        # Imprime el mensaje recibido como argumento.
        print(mensaje)
	a = a + 1
	print("a")
        # Agrega un retraso de 1 segundo antes de la siguiente iteración.
        time.sleep(1)

# Define una función principal llamada main, que contendrá el código principal del programa.
def main():
    # Crea dos procesos: proceso1 y proceso2, que ejecutarán la función imprimir_mensaje con diferentes mensajes.
    proceso1 = multiprocessing.Process(target=imprimir_mensaje, args=("Hola desde el Proceso 1",))
    proceso2 = multiprocessing.Process(target=imprimir_mensaje, args=("Hola desde el Proceso 2",))

    # Inicia los procesos, lo que comienza la ejecución de la función imprimir_mensaje en cada proceso.
    proceso1.start()
    proceso2.start()

    # Espera a que los procesos terminen antes de continuar con el código principal.
    proceso1.join()
    proceso2.join()

    # Imprime un mensaje indicando que los procesos han terminado.
    print("Los procesos han terminado.")

# Verifica si este script se está ejecutando como el programa principal.
if __name__ == "__main__":
    a=10
    # Llama a la función main para iniciar el programa.
    main()
	
