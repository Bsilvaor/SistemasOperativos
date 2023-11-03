import os

def imprimir_pid():
	pid = os.getpid()
	print(f"EL PID de el proceso es: {pid}")

if __name__ == "__main__":
	imprimir_pid()
