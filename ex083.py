#Crie um programa onde o usuario digite uma expressao qualquer que use parenteses. Seu aplicativo devera analisar se a expressao passada esta com os parenteses apertos e fechados em ordem correta.
#print('-=-'*30)
#expressao = input('Digite uma expressao: ')
#print('-=-'*30)
#if expressao.count('(') == expressao.count(')'):
#    print('Sua expressao esta correta! ')
#else:
#    print('Sua expressao esta incorreta')
#print('-=-' * 30)


expr = str(input('Digite uma expressao: '))
pilha = []
for simbolo in expr:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta errada! ')