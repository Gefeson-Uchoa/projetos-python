def linha():
    return '-'*20

def real(valor):
    return f'R${valor:.2f}'.replace('.',',')

def converte_numero(num):
    try:
        return int(num)
    except:
        try:
            return float(num)
        except:
            print('\033[1;31merro de valor, verifique e digite corretamente.\033[m')
            return False
