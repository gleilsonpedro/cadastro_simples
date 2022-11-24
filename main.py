import os
import json
from func_des_cad import *
from tabulate import tabulate




identifica = {
    'inserir' : '\n| # # # # # _____Inserir Usuários_____ # # # # # |\n',
    'ativar' : '\n| # # # # # _____Ativar ou Desativar Usuários_____ # # # # # |\n',
    'editar' : '\n| # # # # # _____Editar Usuários_____ # # # # # |\n',
    'inform_id': '\n| # # # # # _____Informações de Usuários por ID_____ # # # # # |\n',
    'inform_nome': '\n| # # # # # _____Informações de Usuários por Nome_____ # # # # # |\
                    \n| ----- pode buscar por qualquer parte do nome que lembrar ----- |\n',
    'inform_ativos': '\n| # # # # # _____Informações de Usuários Ativos_____ # # # # # |\n',
    'inform_inativos': '\n| # # # # # _____Informações de Usuários Inativos_____ # # # # # |\n',
    'inform_todos': '\n| # # # # # _____Informações de Todos os Usuários_____ # # # # # |\n',
    'sem_cadastro': '\n---> | Desculpe, o Usuário não está cadastrado! |',
    'digitar_errado': '\n---> | Desculpe mas o MENU so aceita Números de 0 a 9! |\n',
    'numero_id': '\n|  Digite o Número da ID ->->->->-> : ',
     'texto_entrada': '\n|  ************************************ MENU ************************************  |\
        \n|  1 - Inserir Usuário                   |  2 - Ativar ou Desativar Usuário        |\
        \n|  3 - Editar o Usuário                  |  4 - Informação de Usuário por ID       |\
        \n|  5 - Buscar Usuário por Nome           |  6 - Informações de Usuários Ativos     |\
        \n|  7 - Informações de Usuários Inativos  |  8 - Informações de Todos os Usuários   |\
        \n|  9 - Limpar a Tela                     |  0 - SAIR                               |\
        \n|----------------------------------------------------------------------------------|\
        \n|  ->->->->-> Digite o Nº ->->->->-> : ',
    'texto_final': '\n|------------------¯\_(ツ)_/¯------------------|\
        \n|_____________ Trabalho em Grupo ______________|\
        \n|  Renato - Nathy - Alysson - Anna - Gleilson  |\
        \n|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\
        \n|-( ͡~ ͜ʖ ͡°)-------Até a Próxima !------( ͡° ͜ʖ ͡°)-|\
        \n|______________________________________________|',
   'finalizacao': '\n| _____________________________________________|\
                   \n| _________ Dados Salvos Com Sucesso _________ |'
}

cadastro = load_base()
escolha = 10
cadastro = load_base()
while escolha != '0':
    escolha = input(identifica['texto_entrada']  ).strip()
    if escolha == '1': #Inserir usuário (novo) 
        print(identifica['inserir'])
        new_user(cadastro)
        continue
    elif escolha == '2': # ativar e desativar usuário
        print(identifica['ativar'])
        num_id = str(input(identifica['numero_id']))
        mudandoStatus(cadastro, num_id)
        continue
    elif escolha == '3': # editar usuário
        print(identifica['editar'])
        num_id = str(input(identifica['numero_id']))
        editar_cad(cadastro, num_id)
        continue
    elif escolha == '4': #informações de um usuário por ID
        print(identifica['inform_id'])
        num_id = str(input(identifica['numero_id']))
        busca_tabela(cadastro, num_id)
        continue
    elif escolha == '5': #Buscar usuário por nome
        print(identifica['inform_nome'])
        nome_busca = input('Insira um nome para busca:').strip().title()
        busca_nome(cadastro,nome_busca)
        continue
    elif escolha == '6': #Informações dos usuários Ativos
        print(identifica['inform_ativos'])
        busca_ativos(cadastro)
        continue
    elif escolha == '7': #Informações dos usuários inativos
        print(identifica['inform_inativos'])
        busca_inativos(cadastro)
        continue
    elif escolha == '8': #Informações de todos os usuário
        print(identifica['inform_todos'])
        busca_todos(cadastro)
        continue
    elif escolha == '9': #Informações de todos os usuário
        limpar_tela()
        continue
    elif escolha == '0': #sai do programa e salva json local
        limpar_tela()
        print(identifica['finalizacao'])
        print(identifica['texto_final'])
        save_base(cadastro)
    else:
        limpar_tela()
        print(identifica['digitar_errado'])   