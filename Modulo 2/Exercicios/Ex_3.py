# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE
cont = 1
qtd = int(input('Quantos filmes deseja adicionar na lista: '))
while cont <= qtd:
     nome = input(f'Digite o nome do {cont}º filme: ')
     cont = cont + 1
     filmes.append(nome)
print(filmes)

# LOOP FOR

qtd = int(input('Quantos filmes deseja adicionar na lista: '))
for cont in range(qtd): 
    nome = input(f'Digite o nome do {cont}º filme: ')
    filmes.append(nome)
print(filmes)




