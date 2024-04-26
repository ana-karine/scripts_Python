# Script de Backup Automático

Este script em Python realiza uma operação de backup automático, copiando arquivos de uma pasta de origem para uma pasta de destino. Ele é útil para manter cópias de segurança de arquivos importantes de forma automatizada.

## Funcionalidades

- **Importação de Bibliotecas**: O script começa importando as bibliotecas necessárias para executar operações de sistema e cópia de arquivos. As bibliotecas utilizadas são `os` e `shutil`.

- **Definição de Origem e Destino**: As variáveis `origem` e `destino` são definidas para indicar os caminhos das pastas de onde os arquivos serão copiados (origem) e para onde serão copiados (destino).

- **Listagem de Arquivos**: O script lista os arquivos presentes na pasta de origem usando a função `os.listdir(origem)` e exibe esses arquivos na saída padrão.

- **Início do Backup**: Após listar os arquivos, o script imprime uma mensagem indicando que o backup está sendo iniciado.

- **Cópia de Arquivos**: O script percorre cada arquivo listado na pasta de origem e copia-o para a pasta de destino utilizando a função `shutil.copy2(caminho_origem, caminho_destino)`. Essa função preserva os metadados dos arquivos, como timestamps.

- **Mensagem de Conclusão**: Finalmente, o script imprime uma mensagem indicando que o backup foi concluído com sucesso.

## Como Usar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Abra um terminal e navegue até o diretório onde o script está localizado.
3. Execute o script com o comando `python nome_do_script.py`.
4. Verifique a pasta de destino para confirmar que os arquivos foram copiados corretamente.

## Observações

- Este script assume que as pastas de origem e destino já existem e têm permissões adequadas de leitura e escrita.
- Certifique-se de revisar e personalizar os caminhos das pastas de origem e destino conforme necessário antes de executar o script.
- Este script pode ser agendado para ser executado periodicamente usando ferramentas como o cron no Linux ou o Agendador de Tarefas no Windows para automatizar o processo de backup.

