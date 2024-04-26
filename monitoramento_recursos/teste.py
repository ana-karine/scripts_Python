import time
import multiprocessing

def consumir_recursos():
    # Consumindo CPU
    while True:
        pass

def consumir_memoria():
    # Consumindo memória
    lista = []
    while True:
        lista.append(' ' * 1024 * 1024)  # Adicionando 1MB à lista
        time.sleep(0.1)  # Aguardando um curto intervalo

if __name__ == "__main__":
    # Criando dois processos separados para consumir CPU e memória
    processo_cpu = multiprocessing.Process(target=consumir_recursos)
    processo_memoria = multiprocessing.Process(target=consumir_memoria)

    # Iniciando os processos
    processo_cpu.start()
    processo_memoria.start()

    # Aguardando um período de tempo para testar o uso de recursos
    time.sleep(30)  # Testando por 30 segundos

    # Terminando os processos
    processo_cpu.terminate()
    processo_memoria.terminate()
