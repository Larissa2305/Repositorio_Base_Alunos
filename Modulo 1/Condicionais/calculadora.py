print('|',30*'-')
print('| Calculadora')
print('|',30*'-')
print('| 1 - Soma')
print('| 2 - Subtração')
print('| 3 - Multiplicação')
print('| 4 - divisão')
print('|',30*'-')
opcoe = int(input('| Escolha uma das opções: '))
num1 = int(input('| Digite o primeiro número: '))
num2 = int(input('| Digite o segundo número: '))
if opcoe == 1:
    print(f'| O resultado é: {num1 + num2}')

elif opcoe == 2:
    print(f'| O resultado é: {num1 - num2}')

elif opcoe == 3:
    print(f'| O resultado é: {num1 * num2}')

elif opcoe == 4:
    print(f'| O resultado é: {num1 / num2}')

else:
    print('| Número errado!')  

        

