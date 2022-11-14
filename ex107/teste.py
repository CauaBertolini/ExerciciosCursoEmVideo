from ex107 import moeda

n = float(input('Digite um valor monetário: R$'))
pa = float(input('Digite uma porcentagem de aumento: '))
pd = float(input('Digite uma porcentagem de redução: '))
print(f'O valor dado foi {n}, seu dobro é {moeda.dobro(n)}, sua metade é {moeda.metade(n)}, com {pa:.0f}% de aumento fica {moeda.aumentar(n, pa)} e com {pd:.0f}%\n'
      f'de redução fica {moeda.diminuir(n, pd)}')
