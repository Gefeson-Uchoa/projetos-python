'''ver se ja existe a basa ok
abrir a base  ok
criar um loop para o usuario cadastrar os produtos
criar uma funcao para formatar os valores
verificar loop
mostrar dados na tela por fim
'''
from modulos import linha,converte_numero,real

#abrir arquivo e organizar
file = open('base_de_dados.txt', 'w+')
file.write(f'{linha()}\n')
file.write('CADASTRO DE PRODUTOS\n')
file.write(f'{linha()}\n')
file.seek(0)
print(file.read())

#cadastra os valores com o usuario
while True:
    while True:
        produto=input('Produto: ')+' '*10
        valor= input('Preço: ').replace(',','.')#colocando , caso o criente digite , nos preços
        valor=converte_numero(valor)
        if False:
            pass
        else:
            break

    file.write(f'{produto[:8]}:{real(valor):>11}\n')

    continua=input('Deseja continuar[S/N]: ').upper()
    print('')
    if continua[0]=='N':
        break



file.seek(0)
print(file.read())

