pessoa={}
galera=[]
while True:
    pessoa.clear()
    pessoa['nome']= input('nome: ')
    while True:
        pessoa['sexo']= input('sexo [M|F]: ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F.)')
    pessoa['idade']=int(input('idade: '))
    galera.append(pessoa.copy())
    while True:
        resp=input('quer continuar: [S|N]: ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda so S ou N. ')
    if resp=='N':
        break
print('=-'*30)
print(galera)