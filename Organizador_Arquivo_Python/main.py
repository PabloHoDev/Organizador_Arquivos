import os
import shutil

# Mapeamento de extensões para pastas
EXTENSOES = {
    'PDFs': ['.pdf'],
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Planilhas': ['.xlsx', '.xls', '.csv'],
    'Textos': ['.txt', '.docx'],
    'Compactados': ['.zip', '.rar']
}

def criar_pasta(caminho):
    if not os.path.exists(caminho):
        os.makedirs(caminho)

def organizar_arquivos(pasta_origem):
    arquivos = os.listdir(pasta_origem)

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta_origem, arquivo)

        if os.path.isfile(caminho_arquivo):
            _, extensao = os.path.splitext(arquivo)

            for pasta, extensoes in EXTENSOES.items():
                if extensao.lower() in extensoes:
                    pasta_destino = os.path.join(pasta_origem, pasta)
                    criar_pasta(pasta_destino)
                    shutil.move(caminho_arquivo, pasta_destino)
                    print(f'Movido: {arquivo} → {pasta}')
                    break

def main():
    pasta = input('Digite o caminho da pasta a ser organizada: ').strip()

    if os.path.exists(pasta):
        organizar_arquivos(pasta)
        print('\nOrganização concluída!')
    else:
        print('Pasta não encontrada.')

if __name__ == '__main__':
    main()
