'''

 Revisão
    -Listas
    -Tuplas
    -Dicionário

'''
#Tupla
# É um tipo de lista imutável

'''

semana = ('segunda', 'terça', 'quarta', 'quinta', 'sexta')

print(semana[2])

print()

print(semana[1:3])

print()

for i in semana:
    print(i)

print('\n-------------------------------------\n')

#Listas
# É um tipo de lista manipulável

comidas = ['lasanha', 'churrasco', 'batata frita']

for i in comidas:
    print(i)

comidas.append('sorvete')    
comidas.append('coca')

print()

for i in comidas:
    print(i)

print()

comidas.remove('sorvete')

for i in comidas:
    print(i)

print() 

comidas.pop(2) # remove um item da lista via posição da matriz

for i in comidas:
    print(i)

print()

'''
# Dict (dicionário)
# Dicionários funcionam com formato:
#   Chave <--> Valor

cliente1 = {
    'nome':'Larissa',
    'idade': 15,
    'empresa':'Senai',
}

cliente2 = {
    'nome':'Marley',
    'idade': 5,
    'empresa':'Sono',
}

print(cliente1['empresa'])