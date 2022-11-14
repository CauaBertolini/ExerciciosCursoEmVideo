#Crie uma Tupla preenchida com os 20 primeiros colocados da tabela do CAMPEONATO BRASILEIRO DE FUTEBOL, na ordem da colocaçao mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os ultimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabetica.
# D) Em que posiçao na tabela esta o time da chapecoense.
rank = ('Palmeiras', 'Cruzeiro', 'Gremio', 'Santos', 'Corinthians', 'Flamengo', 'Atletico Mineiro', 'Athletico Paranaense', 'Internacional', 'Chapecoense', 'Bota Fogo', 'Sao Paulo', 'Fluminense', 'Vasco da Gama', 'Bahia', 'Sport', 'Vitoria', 'Ponte Preta', 'America', 'Coritiba')
print('-=-' * 30)
print('20 Primeiros Colocados da CBF 2019')
print('-=-' * 30)
print(f'''Os 5 primeiros colocados da CBF 2019 sao:
1º {rank[0]}
2º {rank[1]}
3º {rank[2]}
4º {rank[3]}
5º {rank[4]}''')
print('-=-'*30)
print(f'Os 4 ultimos colocados sao: {rank[-4:]}')
print('-=-' * 30)
print(f'Em ordem alfabetica a lista dos 20 primeiros colocados da CBF e a seguinte: {sorted(rank)}')
print('-=-' * 30)
print(f'O Chapecoense se encontra na {rank.index("Chapecoense") + 1}ª Posiçao')
print('-=-' * 30)