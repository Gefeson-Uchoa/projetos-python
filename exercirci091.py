from random import randint
jogo={}
print('=====sorteio=====')
jogo['jogador 1']= randint(1,6)
jogo['jogador 2']= randint(1,6)
jogo['jogador 3']= randint(1,6)
jogo['jogador 4']=randint(1,6)
for c in sorted(jogo, key=jogo.get):
    print(c, jogo[c])
print('o vencedor foi ', end='')
print(max(jogo, key=jogo.get))