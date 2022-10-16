# 15.436.940/0001-03 cnpj da empresa amazon, pegue da internet
#verificando se o usuario digitou corretamente
while True:
    try:
        CNPJ=input('CNPJ: ').strip()
        cnpj=CNPJ.replace('.','')
        cnpj=cnpj.replace('-','')
        cnpj=cnpj.replace('/','')

        #verificando o primeiro digito
        soma_digitos=0
        decremento=5


        for cont,digito in enumerate(cnpj):
            soma_digitos+=int(digito)*decremento
            if cont==11:
                break
            if decremento==2:
                decremento=10
            decremento-=1

        digito01= 11-(soma_digitos % 11)
        if digito01>9:
            digito01=0


        #verificando segundo digito
        soma_digitos=0
        decremento=6

        #verificando segundo digito
        for cont,digito in enumerate(cnpj):
            soma_digitos+=int(digito)*decremento
            if cont==12:
                break
            if decremento==2:
                decremento=10
            decremento-=1

        digito02= 11-(soma_digitos%11)
        if digito02>9:
            digito02=0
        if digito02==int(cnpj[13]) and len(cnpj)==14:
            print('CNPJ valido!')
        else:
            print('CNPJ invalido!')
        break
    except:
        print('erro, verifique os digitos e tente novamente.')
