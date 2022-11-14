#Crie um pequebo sistema modularizado que permita cadastrar pessoas
#pelo seu nnome e idade em um arquivo de texto simples.
#O sistema só vai ter duas opções: cadastrar uma nova pessoa e
#listar todas as pessoas cadastradas.
from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    print('Arquivo não encontrado! Criando novo arquivo...')
    sleep(3)
    criarArquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pesssoa', 'Sair do Programa'])
    if resposta == 1:
        #Opção de fazer a leitura de arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar nova pessoa ao arquivo
        cabeçalho('Cadastro de Nova Pessoa')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida...\033[m')
    sleep(2)
