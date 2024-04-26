import time
import psutil

# Definindo os limites para o uso de CPU e memória por processo
limite_cpu = 5 # Em percentagem (5% para fins didáticos)
limite_memoria = 4  # Em percentagem (5% para fins didáticos)

def monitorar_processos():
    while True:
        # Obtendo a lista de todos os processos e suas informações
        for processo in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            pid = processo.info['pid']
            nome = processo.info['name']
            uso_cpu = processo.info['cpu_percent']
            uso_memoria = processo.info['memory_percent']

            # Verificando se o uso de CPU ou memória excede os limites definidos
            if uso_cpu > limite_cpu:
                print(f"ALERTA: O processo {nome} (PID: {pid}) está utilizando {uso_cpu}% da CPU.")
            if uso_memoria > limite_memoria:
                print(f"ALERTA: O processo {nome} (PID: {pid}) está utilizando {uso_memoria}% da memória.")

        # Aguardando um intervalo de tempo antes da próxima verificação
        time.sleep(5)  # Verificando a cada 5 segundos

if __name__ == "__main__":
    monitorar_processos()
