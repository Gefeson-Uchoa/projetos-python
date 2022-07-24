try:
    #recebendo e verificando se o usuario digitou corretamente

    CPF = input('CPF: ').strip()
    cpf = CPF.replace('.','')
    cpf = cpf.replace('-','')

    #somando numeros para a verificaçao 077.819.653-45
    #verificando primeiro digito

    soma_de_digitos=0
    decremento = 10
    for c in cpf:
        soma_de_digitos+=int(c)*decremento
        if decremento == 2:
            break
        decremento-=1

    digito01=11-(soma_de_digitos % 11)
    if digito01>9:
        digito01=0

    #verificando segundo digito
    soma_de_digitos02=0
    decremento02=11
    for c in cpf:
        soma_de_digitos02+=int(c)*decremento02
        if decremento02 == 2:
            break
        decremento02-=1

    digito02=11-(soma_de_digitos02 % 11)
    if digito02>9:
        digito02=0
    if digito02==int(cpf[10]):
        print(f'{CPF} é um cpf valido!')
    else:
        print('cpf invalido')

except:
    print('houve algum erro, verifique os dados e tente novamente.')