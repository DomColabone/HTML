import os
from prettytable import PrettyTable

def get_size(path):
    """Retorna o tamanho total dos arquivos e diretórios dentro do caminho especificado."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(filepath)
            except OSError:
            
                continue
    return total_size

def list_large_files(path, threshold_mb=100):
    """Lista arquivos maiores que o limite especificado (em MB)."""
    large_files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(filepath) / (1024 * 1024)
                if file_size > threshold_mb:
                    large_files.append((filepath, file_size))
            except OSError:

                continue
    return large_files

def print_report(path):
    """Gera um relatório de uso de espaço e arquivos grandes."""
    total_size = get_size(path)
    large_files = list_large_files(path)
    
    print(f"Uso total de espaço em '{path}': {total_size / (1024 * 1024):.2f} MB")
    
    if large_files:
        print("\nArquivos maiores que o limite especificado:")
        table = PrettyTable()
        table.field_names = ["Caminho do Arquivo", "Tamanho (MB)"]
        for file_path, file_size in large_files:
            table.add_row([file_path, f"{file_size:.2f}"])
        print(table)
    else:
        print("\nNenhum arquivo grande encontrado.")

if __name__ == "__main__":
    path = input("Digite o caminho do diretório a ser analisado: ")
    print_report(path)

python analisador_espaco.py
