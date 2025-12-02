import os
import json

with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
    tarefas = json.load(arquivo)

def mostrar_tarefas():
    barra = f'|{60*'-'}|'
    print(barra)
    for i in range(len(tarefas['tarefas'])):
        print(f'| {i+1} - Tarefa: {tarefas['tarefas'][i]} | Data: {tarefas['datas'][i]}')
    input('| Aperte "ENTER" para contuinuar...')

def adicionar_tarefas():
    barra = f'|{60*'-'}|'
    print(barra)
    tarefa = input('| Nome da tarefa: ')
    data = input('| Data: ')
    tarefas['tarefas'].append(tarefa)
    tarefas['datas'].append(data)
    print('| Tarefa adicionada com sucesso!')
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

    input('| Aperte "ENTER" para contuinuar...')

def remover_tarefas():
    barra = f'|{60*'-'}|'
    print(barra)
    for i in range(len(tarefas['tarefas'])):
        print(f'| {i+1} - Tarefa: {tarefas['tarefas'][i]} | Data: {tarefas['datas'][i]}')
    id_tarefa = int(input('| Digite o número da tarefa que deseja remover: '))
    
    if id_tarefa > 0:
        tarefa = tarefas['tarefas'].pop(id_tarefa-1)
        tarefas['datas'].pop(id_tarefa-1)  
    else:
        print('| ID inválido.')
              
    print(f'| Tarefa "{tarefa}" removida com sucesso!')
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
        
    input('| Aperte "ENTER" para contuinuar...')

def menu():
    while True:
        try: 
            os.system('cls')
            barra = f'|{60*'-'}|'
            print(barra)
            print('| GERENCIADOR DE TAREFAS')
            print(barra)
            print('| 1 - Mostrar tarefa')
            print('| 2 - Adicionar tarefa')
            print('| 3 - Remover tarefa')
            print('| 4 - Sair')
            print(barra)
            opc = int(input('| Escolha uma opção: '))
            if opc == 1:
                os.system('cls')
                mostrar_tarefas()
            elif opc == 2:
                os.system('cls')
                adicionar_tarefas()
            elif opc == 3:
                os.system('cls')
                remover_tarefas()                
            elif opc == 4:
                print('| Saindo do programa...')
                break
            else:
                os.system('cls')
                print('| Opção inválida')
                input('| Aperte "ENTER" para contuinuar...')
        except:
            print('| ERRO! Escolha uma opção válida')
            input('| Aperte "ENTER" para contuinuar...')       
    
menu()               