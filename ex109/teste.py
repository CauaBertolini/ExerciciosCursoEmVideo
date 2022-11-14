from ex109 import moeda
n = float(input('Digite um valor monetário: R$ '))
pa = float(input('Digite uma porcentagem de aumento: '))
pd = float(input('Digite uma porcentagem de redução: '))
print(f'O valor dado foi {moeda.moedas(n)}')
print(f'Seu dobro é {moeda.dobro(n, True)}')
print(f'Sua metade é {moeda.metade(n, True)}')
print(f'Com {pa}% de aumento fica {moeda.aumentar(n, pa, True)}')
print(f'Com {pd}%\n de redução fica {moeda.diminuir(n, pd, True)}')
