import json

with open('senha.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

email = input('Digite o email: ')
senha = input('Digite a senha: ')

if email == dados['email'] and senha == dados['senha']:
    print('Acesso liberado!')
else:
    print('Acesso negado!')
    
 











 
 
 
 
