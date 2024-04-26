import os

ajustar_permissões_backup = "/home/ana/Documents/scripts/backup_automatico/arquivos_destino"

for raiz, diretorios, arquivos in os.walk(ajustar_permissões_backup):
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(raiz, arquivo)
        # Definindo permissões para leitura e execução, mas não escrita
        os.chmod(caminho_arquivo, 0o750)
        print(f"Permissões ajustadas para {caminho_arquivo}")
