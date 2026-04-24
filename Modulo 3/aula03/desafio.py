# Crie um conversor de
#       Real - Dólar
#       Dólar - Real
#       Real - BTC (Bitcoin)
import time

while True:    
    try:
        print()
        print('Conversor')
        print("-"*15)
        print('1 - Real')
        print('2 - Dollar')
        print('3 - Bitcoin')

        opcao = int(input('Digite a opção: '))
        taxa_dollar = 5.02
        taxa_btc = 366590

        if opcao == 1:
            qtd = float(input('Qual valor em reais: '))
            valor1 = qtd*taxa_dollar
            print(f'\nO valor em dollar é: {valor1:.2f}\n')

        elif opcao == 2:
            qtd = float(input('Qual valor em dollar: '))
            valor2 = qtd/taxa_dollar
            print(f'\nO valor em reais é: {valor2:.2f}\n')

        elif opcao == 3:
            qtd = float(input('Qual valor em BTC: '))
            valor3 = qtd/taxa_btc
            print(f'\nO valor em BTC é: {valor3:.2f}\n')  

        elif opcao == 0:
            print('\nObrigado por usar nossos serviços\n')
            break    

        else:
            print('ERRO')
            continue          

    except:
        ValueError(print('\nDigite apenas números'))
        KeyboardInterrupt(print('Obrigado'))        
