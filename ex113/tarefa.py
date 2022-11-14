#Reescreva a função leiaInt() que fizemos no desafio 104,
#incluindo agora a possibilidade da digitação de um número
#de tipo inválido. Aproveite e crie também uma função
#leiaFloat() com a mesma funcionalidade.

def leiaInt(msg = 'Digite um número: '):
    print('-=-'*10)
    print('Bem vindo ao Leia Int!'.center(30))
    print('-=-'*10)
    válido = False
    while not válido:
        try:
            valor = str(input(msg)).strip().replace(',', '.')
            valorf = float(valor)
            valorFinal = round(valorf)
            int(valorFinal)
        except(ValueError, TypeError):
            print(f'\033[31mO valor "{valor}" não é um valor do tipo numérico! Tente novamente.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[35mO usuário preferiu não informar nenhum valor.\033[m')
            continue
        except:
            print(f'\033[31m"{valor}" não é um valor válido! Tente novamente.\033[m')
            continue
        else:
            válido = True
    print('-=-'*10)
    print(f'Você digitou o número {valorFinal}'.center(30))
    print('-=-'*10)


def leiaFloat(msg='Digite um número real: '):
    print('=-='*10)
    print('Bem vindo ao Leia Float!'.center(30))
    print('=-='*10)
    válido = False
    while not válido:
        try:
            numero = input((msg)).strip().replace(',', '.')
            numeroFloat = float(numero)

        except (ValueError, TypeError):
            print(f'\033[31mO valor "{numero}" não é um valor do tipo númérico! Tente novamente.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[35mO usuário preferiu não informar nenhum valor.\033[m')
            continue
        except:
            print(f'\033[31mO valor "{numero}" é inválido! Tente novamente.\033[m')
            continue
        else:
            válido = True
    print('=-='*10)
    print(f'Você digitou o número {numeroFloat:.2f}'.center(30))
    print('=-='*10)


n1 = leiaInt()
n2 = leiaFloat()
print(f'O valor inteiro digitado foi {n1} e o valor real foi {n2}')
