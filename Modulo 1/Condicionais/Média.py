
print('|',40*'_','|')
print('| SISTEMA DE PROVAS')
print('|',40*'_','|')
nome = input('| Digite o seu nome: ')
nota1 = float(input('| Digite a nota da primeira prova: '))
nota2 = float(input('| Digite a nota da segunda prova: '))
nota3 = float(input('| Digite a nota da terceira prova: '))
print('|',40*'_','|')
media = round((nota1+nota2+nota3)/3,1)
print(f'| Aluno: {nome} | Aprovado? {media >= 5}')
if media >= 5:
    print('Aprovado!')
else:
    print('Reprovado')    