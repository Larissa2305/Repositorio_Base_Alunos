modelo = input('Qual foi o modelo do carro? ')
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro rodou? '))

valor = 0

if modelo == 'bmw':
    valor = 300
elif modelo == 'audi':
    valor = 200
elif modelo == 'fusca':
    valor = 80  
else:
    valor = 10

valor_dias = (dias * valor)
valor_km = (km * 0.15)
valor_total = (valor_dias + valor_km)
print(f'você andou {km}km por {dias} dias, então o preço a pagar é R${valor_total}.')
