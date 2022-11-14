# Escreva um programa que leia um valor em metros e o exiba em centimetros e milimetros
m = float(input('\033[34mDigite a medida em metros: '))
dm = m * 10
cm = m * 100
mm = m * 1000
dam = m / 10
hm = m / 100
km = m / 1000
print('\033[35m{} metros tem:\n\033[36m{:.0f} decimetros.\n{:.0f} centimetros.\n{:.0f} milimetros.\n{} decametros.\n{} hectometros.\n{} quilometros.'.format(m, dm, cm, mm, dam, hm, km))
