# importando as bibliotecas
import os
import shutil

# definindo origem e destino
origem = "/home/ana/Documents/scripts/backup_automatico/arquivos_origem"
destino = "/home/ana/Documents/scripts/backup_automatico/arquivos_destino"

# listando arquivos a serem copiados
arquivos = os.listdir(origem)

# exibindo os arquivos listados
print("Arquivos da pasta de origem:")
for arquivo in arquivos:
    print(arquivo)

print("\nIniciando backup...")

# copiando arquivos
for arquivo in arquivos:
    caminho_origem = os.path.join(origem, arquivo)
    caminho_destino = os.path.join(destino, arquivo)
    shutil.copy2(caminho_origem, caminho_destino)

print("\nBackup concluído com sucesso!")
