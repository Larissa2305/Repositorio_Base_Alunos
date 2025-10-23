# Utilize um loop while e um loop for para percorrer a lista e exibir os valores dos items contidos na lista

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

frutas = ['maçã', 'banana', 'morango', 'uva', 'laranja','abacaxi']

# LOOP WHILE
cont = 0
while cont < len(frutas):
    print(frutas[cont])
    cont+=1

# LOOP FOR

for fruta in frutas:
    print(f'Fruta: {fruta}')

