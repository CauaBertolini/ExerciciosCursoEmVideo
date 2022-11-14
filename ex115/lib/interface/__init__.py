colorir = ['\033[30m',
       '\033[31m',
       '\033[32m',
       '\033[33m',
       '\033[34m',
       '\033[34m',
       '\033[35m',
       '\033[36m',
       '\033[37m',
       '\033[m',]


def leiaInt(msg='Digite um número: '):
    while True:
        try:
            valor = (input(msg))
            int(valor)
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
            return int(valor)


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt, cor=7):
    print(linha())
    print(f'{colorir[cor]}{txt.center(42)}{colorir[8]}')
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    contador = 1
    for opc in lista:
        print(f'\033[33m{contador} \033[m- \033[34m{opc}\033[m')
        contador += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc