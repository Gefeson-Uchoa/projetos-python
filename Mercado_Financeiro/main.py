# entrar no site do mercado financeiro
# consutar açoes -- criar uma lista com cada açao a pesquisar
# retornar = valor, subiu ou desceu
#
#


from time import sleep
from classes import AutoChrome


chrome = AutoChrome()
chrome.EntraSite('https://www.google.com/finance/')
chrome.PesquisaAcao('petr4')
a = chrome.ValorAcao()
with open('arquivo.txt','w+') as p:
    p.write(f'R${a}')

sleep(5)
