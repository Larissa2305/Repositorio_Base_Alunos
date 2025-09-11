print('SISTEMA DE PROVAS')
cont = 1
soma = 0
qtd_provas = int(input('Quantas provas o aluno realizou? '))
while cont <= qtd_provas:
    nota = float(input(f'Digite a nota da prova {cont}: '))
    cont += 1
    soma += nota

media = soma/qtd_provas    
print(f'O aluno obteve a média de: {media}')    