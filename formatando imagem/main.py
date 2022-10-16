import os
from PIL import Image


def main(caminho, nova_largura=800):
    if not os.path.isdir(caminho):
        raise NotADirectoryError(f'{caminho} nao existe')

    for raiz, pastas, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            nome = os.path.join(raiz,arquivo)
            novo_nome, ext = os.path.splitext(arquivo)
            new_tag = 'new'
            novo_arquivo = novo_nome+new_tag+ext
            novo_caminho_arquivo = os.path.join(raiz,novo_arquivo)
            if os.path.isfile(novo_caminho_arquivo):
                print(f'arquivo {novo_arquivo}, ja existe.')
                continue

            if new_tag in nome:
                continue

            img_pillow = Image.open(nome)    # essa area ta destina a fazer a conversao
            width, height = img_pillow.size
            nova_altura = round(nova_largura*height/width)

            print(nova_altura,width,nova_largura,height)
            nova_imagem = img_pillow.resize((nova_largura,nova_altura),Image.Resampling.LANCZOS)
            nova_imagem.save(novo_caminho_arquivo,optimize=True,quality=70)

            nova_imagem.close()
            img_pillow.close()
            #os.remove(nome)  # apaga os arquivos originais. so se nescessario

if __name__ == '__main__':
    caminho = '/home/junior-buffon/Documentos/BLOG2'  # voce bota o caminho da sua pasta
    main(caminho,800)