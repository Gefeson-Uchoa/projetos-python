'''
um app que mostra todos os arquivos e algumas informaçoes mesmo dentro de outros diretorios desde que no caminho certo,
digite o termo que voce deseja proucurar, uma boa funcionalidade seria buscar .mp3, .jpg, .py, .html entre outros
'''

import os


caminho = input('Digite um Caminho: ')
termo = input('digite o termo que deseja proucurar: ')
def FormatacaoDeTamanho(tamanho):
    base = 1024
    kilo = base
    mega = base**2
    giga = base**3
    tera = base**4
    peta = base**5
    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'

cont = 0
for raiz,diretorio,arquivos in os.walk(caminho):
    for arquivo in arquivos:
        if termo in arquivo:
            try:
                cont+=1
                caminho_completo = os.path.join(raiz,arquivo)  # mostra o caminho completo
                nome_do_arquivo, ext_do_arquivo = os.path.splitext(arquivo) #pega o nome com a extençao do arquivo
                tamanho = os.path.getsize(caminho_completo)
                print(f'encontrei o arquivo :{arquivo}\n'
                      f'caminho: {caminho_completo}\n'
                      f'nome: {nome_do_arquivo}\n'
                      f'extençao: {ext_do_arquivo}\n'
                      f'tamaho: {tamanho}\n'
                      f'tamanho formatado: {FormatacaoDeTamanho(tamanho)}\n')
            except PermissionError as e:
                print('sem permissoes.')
            except FileNotFoundError as f:
                print('arquivo nao encontrado.')
            except Exception as e:
                print('erro desconhecido')

print(f'{cont} - arquivo(s) encontrados.')