import random
import os
#IMPORTAMOS EL MÓDULO RANDOM ( proporciona la posibilidad de producir números aleatorios)
#Y EL MÓDULO OS (permite que podamos crear en el escritorio un archivo ranking.txt que guarde los rankings)

#Definimos la clase ranking
class Ranking:
    def __init__(self):
        self.array = []
        # ESTO DE ABAJO ES UN FUSILAMIENTO DE MANUAL, PERO NO CONSEGUÍA ENCONTRAR LA MANERA DE QUE SE CREARA EL .TXT 
        # y entre STACK Y CHAT LO HAN HECHO (A LA DUODÉCIMA)
        # Utilizamos os.path.expanduser para obtener la ruta al escritorio del usuario
        self.nombre_fichero = os.path.join(os.path.expanduser('~'), 'Desktop', 'ranking.txt')

#Definimos
    def push(self, jugador, intentos):
        self.array.append((jugador, intentos))
        line_to_write = f"{jugador} - {intentos} intentos\n"
        return line_to_write

    def write_file(self, line_to_write):
        with open(self.nombre_fichero, "a") as f:
            f.write("\n")
            f.write(line_to_write)
            f.write("\n")

    def read_file(self):
        with open(self.nombre_fichero, "r") as f:
            print(f.read())

    def vaciar_ranking(self):
        with open(self.nombre_fichero, "w") as f:
            f.truncate(0)

class Minijuego:
    def __init__(self, ranking):
        self.ranking = ranking

    def jugarpartida(self):
        jugador_actual = input("Ingresa tu nombre de jugador(SI PONES ALGO OTAKU TU PC SE AUTODESTRUIRÁ): ")
        numero_aleatorio = random.randint(1, 10)
        intentos = 0

        while intentos < 5:
            intento = int(input("Adivina el número (1-10): "))
            intentos += 1

            if intento == numero_aleatorio:
                print(f"¡Correcto! CRACK, FIGURA, MASTODONTE! Has adivinado en {intentos} intento/s. DENLE YA EL GRADUADO!")
                self.ranking.write_file(self.ranking.push(jugador_actual, intentos))
                break
            else:
                if intento < numero_aleatorio:
                    print("MEC! Incorrecto. El número que debes adivinar es mayor.")
                else:
                    print("MEC! Incorrecto. El número que debes adivinar es menor.")

        if intentos == 5:
            print(f"Lo siento, has agotado tus 5 intentos. El número era {numero_aleatorio}. TE DIRÍA QUE MÁS SUERTE LA PRÓXIMA...")

if __name__ == "__main__":
    ranking = Ranking()
    juego = Minijuego(ranking)

    while True:
        print("1) LETS GOO (JUGAR PARTIDA)")
        print("2) Ver ranking")
        print("3) RESET ranking")
        print("4) Salir")

        try:
            opcion_elegida = int(input("Selecciona una opción (1-4): DEL 1 AL 4! NO PONGAS ALCACHOFA "))
        except ValueError:
            print("Ingresa un número válido penas, que eres un penas.")
            continue

        if opcion_elegida == 1:
            juego.jugarpartida()
        elif opcion_elegida == 2:
            ranking.read_file()
        elif opcion_elegida == 3:
            ranking.vaciar_ranking()
            print("El ranking ha sido reseteado.")
        elif opcion_elegida == 4:
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("ESPABILA, QUE NO TE ENTERAS! OPCIÓN NO VALIDA.")
