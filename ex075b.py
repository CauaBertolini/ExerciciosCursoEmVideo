nums = (int(input('Digite um numero: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite mais um numero: ')),
        int(input('Digite um ultimo numero: ')))
print(f'Voce digitou os valores: {nums}')
print(f'O valor nove apareceu {nums.count(9)} vezes.')
if 3 in nums:
    print(f'O valor 3 apareceu na {nums.index(3)+1}° Posiçao')
else:
    print('O valor 3 nao foi digitado em nenhuma posiçao')
for n in nums:
    if n % 2 == 0:
        print(n, end=' ')