try:
    def linha():
        print('='*19)

    from time import sleep
    #recebendo valor pelo caixa
    linha()
    nome01='CAIXA ELETRONICO '
    print(f'{nome01:=^19}')
    linha()
    valor_saque=float(input('valor: '))

    print('contabilizando notas.')
    sleep(1)

    notas=[100,50,20,10,5,2]
    notas_sacadas=[]
    #fazendo a escolha das cedulas
    for c in notas:
        notas_disponiveis=[int(valor_saque//c)]
        copia=notas_disponiveis.copy()
        notas_sacadas.append(copia)
        valor_saque=valor_saque%c

    linha()
    for cont,c in enumerate(notas_sacadas):
        for indice,n in enumerate(notas):
            if cont==indice:
                cedulas=notas[indice]

        if c!=[0]:
            print(f'{c} Nota(s) de: {cedulas}')

    linha()
    if valor_saque!=0:
        print(f'\nsaldo em conta = {valor_saque:.2f}\n'
              f'nao suportamos moedas.')

except:
    print('erro,verifique o valor e tente novamente.')