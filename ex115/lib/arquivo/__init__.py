from ex115.lib.interface import *

def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'Houve um ERRO ao tentar criar o arquivo {nome}')
    else:
        print(f'Arquivo {nome} criado com êxito!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'Houve um ERRO ao tentar ler o arquivo {nome}')
    else:
        cabeçalho('Pessoas Cadastradas')
        #Este for basicamente lê cada "cadastro individual" colocado no arquivo cursoemvideo.txt
        #ELe usa o ";" como carácter de divisão Split(';') então transformando 'Cauã;16\n' em 'Cauã' '16\n'
        #'Cauã' == dado[0]
        #'16\n' == dado[1]
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='Desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'Houve um ERRO ao tentar abrir o arquivo {arquivo}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'Houve um ERRO ao escrever o novo registro no arquivo {arquivo}')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()