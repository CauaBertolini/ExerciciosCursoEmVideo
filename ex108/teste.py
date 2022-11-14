from ex108 import moeda
n = float(input('Digite um valor monetário: R$ '))
pa = float(input('Digite uma porcentagem de aumento: '))
pd = float(input('Digite uma porcentagem de redução: '))
print(f'O valor dado foi {moeda.moedas(n)} seu dobro é {moeda.moedas(moeda.dobro(n))} sua metade é {moeda.moedas(moeda.metade(n))} com {pa}% de aumento fica {moeda.moedas(moeda.aumentar(n, pa))} e com {pd}%\n'
      f'de redução fica {moeda.moedas(moeda.diminuir(n, pd))}')
