import os
import shutil
def move(caminho,caminho_novo):
    for root, dirc, files in os.walk(caminho):
        for file in files:
            old_file = os.path.join(root, file)
            new_file = os.path.join(caminho_novo, file)
            shutil.move(old_file, new_file)

def moveE(caminho,caminho_novo,artigo): # arquivos Especificos
    for root, dirc, files in os.walk(caminho):
        for file in files:
            old_file = os.path.join(root, file)
            new_file = os.path.join(caminho_novo, file)
            if artigo in file:
                shutil.move(old_file, new_file)

def copy(caminho,caminho_novo):
    for root, dirc, files in os.walk(caminho):
        for file in files:
            old_file = os.path.join(root, file)
            new_file = os.path.join(caminho_novo, file)
            shutil.copy(old_file, new_file)

def copyE(caminho,caminho_novo,termo):
    for root, dirc, files in os.walk(caminho):
        for file in files:
            old_file = os.path.join(root, file)
            new_file = os.path.join(caminho_novo, file)
            if termo in file:
                shutil.copy(old_file, new_file)

def excluir(caminho):
    for root, dirc, files in os.walk(caminho):
        for file in files:
            old_file = os.path.join(root, file)
            os.remove(old_file)

def excluirE(caminho,especifico):   # arquivos especificos
    for root, dirc, files in os.walk(caminho):
        for file in files:
            old_file = os.path.join(root, file)
            if especifico in file:
                os.remove(old_file)

def linha():
    print('=-='*10)

def especifico():
    especifico = int(input('[1] - selecionar todos: \n'
                           '[2] - arquivos especificos:\n'
                           'opçao: '))
    return especifico


def continuar():
    continua = int(input('deseja continuar[1-sim] [2-nao]: '))
    return continua

