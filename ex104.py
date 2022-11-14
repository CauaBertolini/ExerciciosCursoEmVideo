#Crie um programa que tenha a função leiaInt(). que vai funcionar de forma semelhante à função input() do Python,
#só que fazendo a validação para aceitar apenas um valor numérico.

#Ex:
#n=leiaInt('Digite um n')
def LeiaInt(mensagem='Digite um número: '):
    print('_'*40)
    n = input(f'{mensagem}')
    n1 = n
    n = n.isnumeric()
    if n == False:
        while n != True:
            print('\033[31mERRO! DIGITE UM NÚMERO INTEIRO.\033[m')
            n = input(f'{mensagem}')
            n1 = n
            n = n.isnumeric()
    return n1


n = LeiaInt('Digite um número: ')
print(f'\033[34mVocê digitou o número {n}')
