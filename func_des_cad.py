import os
import json
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
    'sem_cadastro': '\n ---> | Desculpe, o Usuário não está cadastrado! |',
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
#               ***** FUNÇÕES *****
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear") 
    pass

# LER E ABRIR BASE DE DADOS EM JSON
def load_base():
    caminho = os.path.join(os.getcwd(),'contatos.json')
    cadastro = {}
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            cadastro = json.load(arquivo)
    return cadastro

# SALVAR SUBESCREVENDO BASE DE DADOS EM JSON
def save_base(cadastro):
    caminho = os.path.join(os.getcwd(),'contatos.json')
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(cadastro, arquivo, indent=4, ensure_ascii=False)

# ADICIONA USUÁRIO - inserindo usuario e se for repetido so mudar para True falta so fazer a função
def new_user(cadastro, Status=True, Telefone='Não Informado', Endereço='Não Informado'):
    '''Adiciona cadastro com ID incremental, nome-> obrigatório, telefone e endereço se não informado
        seta como default ->\n (Não Informado), status padrão -> True, se o nome telefone e endereço ja esxisir
        não adiciona só transforma em True(ativo) se o cadastro estiver False(inativo)'''
    ident = len(cadastro)+1
    id = str(ident)
    Nome = str(input('Insira seu Nome: ')).title().strip()
    while True:
        if Nome == '':
            Nome = str(input('Insira um Nome para continuar: ')).title().strip()
        else:
            break
    Telefone = input('Insira seu Telefone: ').strip()
    Endereço = input('Insira seu endereço: ').title().strip()
    if Telefone == '':
        Telefone = 'Não Informado'
    if Endereço == '':
        Endereço = 'Não Informado'
    valida = 1
    for key, value in cadastro.items():
        if Nome == value['Nome'] and Telefone == value['Telefone'] and Endereço == value['Endereço']:
            value['Status'] = True
            valida = 0
            print(f"\n---> | O usuário -> {value['Nome']} já está cadastrado\
                    \n---> | seu Status é Ativo!\n")
    if valida == 1:
        cadastro[id] = {
            'Status': Status,
            'Nome': Nome,
            'Telefone': Telefone,
            'Endereço': Endereço
            }

# MENU PARA ATIVAR E DESATIVAR USUÁRIO
def minimenu_ativaDes(cadastro, **kwargs):
    '''Ativa um Usuário ou desativa inserindo parâmetro\
        \ncadastro, utilizado pela função mudandoStatus'''
    ativa_desativa =  input('Digite | 1 - para ativar | 2 - para desativar o usuário: ').strip()
    while True:
        if ativa_desativa.isdigit() == False or len(ativa_desativa)>1 or ativa_desativa >= '3':
            ativa_desativa = input('Digite | 1 - para ativar | 2 - para desativar o usuário: ').strip()
        elif ativa_desativa == '1':
            ativando = True
            valor_ativando = 'Ativo'
            break 
        elif ativa_desativa == '2':
            ativando = False
            valor_ativando = 'Inativo'
            break
        else:
            continue
    if kwargs['menu_ativa']:
        return ativando, valor_ativando

# MUDAR STATUS JUNTO COM MENU PARA ATIVAR E DESATIVAR
def mudandoStatus(cadastro,chave):
    '''Utiliza a resposta da função minimenu_ativaDes para ativar\
        \n ou desativar o usuário com os parãmetros cadastro e numero de id'''
    print(identifica['ativar'])
    ativando, valor_ativando = minimenu_ativaDes(cadastro, menu_ativa = True )
    while True: 
        if chave in cadastro.keys():
            for key, value in cadastro.items():
                if key == chave:
                    value['Status'] = ativando
                    print(f"\n---> | Usuário -> {value['Nome']}\
                            \n---> | Status  -> {valor_ativando}\n")
            break
        else:
            print(identifica['sem_cadastro'])
            chave = input(identifica['numero_id'])

# EDITA AS INFORMAÇÕES DO CADASTRO POR ID
def editar_cad(cadastro, chave):
    '''Edita cadastro buscando pela ID\
        \n com os parametros cadastro e chave'''    
    submenu_editar = input('Digite para alterar -> 1-NOME | 2-ENDEREÇO | 3-TELEFONE | 4-TUDO:')
    while True:
        if chave in cadastro.keys():
            if submenu_editar.isdigit() == False or len(submenu_editar)> 1 or submenu_editar > '4' or submenu_editar <= '0':
                submenu_editar = input('Digite para alterar -> 1-NOME | 2-ENDEREÇO | 3-TELEFONE: | 4-TUDO:')
            elif submenu_editar == '1': #edita nome
                if chave in cadastro.keys():
                    for key, value in cadastro.items():
                        if key == chave:
                            novo_nome = input('Digite o Novo Nome: ').title().strip()
                            while True:
                                if novo_nome == '':
                                    novo_nome = input('Digite o Novo Nome: ').title().strip()
                                else:
                                    break
                            #value['Status'] = True
                            value['Nome'] = novo_nome
                            print(f"\n---> | Usuário -> {value['Nome']} -> Alterado com sucesso!\n")
                    break
            elif submenu_editar == '2':   # edita endereço
                if chave in cadastro.keys():
                    for key, value in cadastro.items():
                        if key == chave:
                            novo_end = input('Digite o Novo Endereço: ').title().strip()
                            if novo_end == '':
                                value['Endereço'] = 'Não Informado'
                            else:
                                value['Endereço'] = novo_end
                            #value['Status'] = True
                            print(f"\n---> | Usuário -> {value['Nome']}\
                                    \n---> | Endereço -> {value['Endereço']}\
                                    \n---> | Alterado com sucesso!\n")
                    break
            elif submenu_editar == '3': # edita telefone
                if chave in cadastro.keys():
                    for key, value in cadastro.items():
                        if key == chave:
                            novo_tel = input('Digite o Novo Telefone: ')
                            if novo_tel == '':
                                value['Telefone'] = 'Não Informado'
                            else:
                                value['Telefone'] = novo_tel
                            #value['Status'] = True
                            print(f"\n---> | Usuário -> {value['Nome']}\
                                    \n---> | Telefone -> {value['Telefone']}\
                                    \n---> | Alterado com sucesso!")
                    break
            elif submenu_editar == '4': # edita tudo
                if chave in cadastro.keys():
                    for key, value in cadastro.items():
                        if key == chave:
                            novo_nome = input('Digite o Novo Nome: ').title().strip()
                            while True:
                                if novo_nome == '':
                                    novo_nome = input('Digite o Novo Nome: ').title().strip()
                                else:
                                    break
                            novo_end = input('Digite o Novo Endereço: ').title().strip()
                            if novo_end == '':
                                value['Endereço'] = 'Não Informado'
                            else:
                                value['Endereço'] = novo_end
                            novo_tel = input('Digite o Novo Telefone: ')
                            if novo_tel == '':
                                value['Telefone'] = 'Não Informado'
                            else:
                                value['Telefone'] = novo_tel
                            #value['Status'] = True
                            value['Nome'] = novo_nome
                            print(f"\n---> | Usuário -> {value['Nome']}\
                                \n---> | Endereço -> {value['Endereço']}\
                                \n---> | Telefone -> {value['Telefone']}\
                                \n---> | Alterado com sucesso!\n")
                    break
        else:
            print(identifica['sem_cadastro'])
            chave = input(identifica['numero_id'])

# BUSCA CADASTRO PELA ID - busca pela id e printa dados do cadastro
def busca_tabela(cadastro, chave): 
    '''Busca o cadastro passando os parametros "cadastro" e a ID que quer buscar'''
    tabela = []
    headers = ['ID','STATUS','NOME','TELEFONE','ENDEREÇO']
    while True:
        if chave in cadastro.keys():
                for key, value in cadastro.items():
                    if key == chave:
                        tabela.append([
                            key,
                            cadastro[key]['Status'],
                            cadastro[key]['Nome'],
                            cadastro[key]['Telefone'],
                            cadastro[key]['Endereço']
                        ])
                        print(tabulate(tabela, headers, tablefmt="simple_grid"))
                        #print(f"Usuário - {value['Nome']}\nStatus  -> Inativo")
                break
        else:
            print(identifica['sem_cadastro'])
            chave = input(identifica['numero_id'])

# BUSCA PELO NOME
def busca_nome(cadastro, nome_busca):
    ''' Busca nos valores o nome de usuário'''
    nomes=[]
    headers = ['ID','STATUS','NOME','TELEFONE','ENDEREÇO']
    for key, value in cadastro.items():
        if nome_busca in cadastro[key]['Nome']:
            nomes.append([
                    key,
                    cadastro[key]['Status'],
                    cadastro[key]['Nome'],
                    cadastro[key]['Telefone'],
                    cadastro[key]['Endereço']
                ])
    print(tabulate(nomes, headers, tablefmt="simple_grid"))

# LISTA CADASTROS TRUE - busca todos os true
def busca_ativos(cadastro):
    '''Busca todos os cadastros True com o parametro "cadastro"'''
    ativos = []
    headers = ['ID','STATUS','NOME','TELEFONE','ENDEREÇO']
    for key, value in cadastro.items():
        if value['Status'] == True:
            ativos.append([
                key,
                cadastro[key]['Status'],
                cadastro[key]['Nome'],
                cadastro[key]['Telefone'],
                cadastro[key]['Endereço']
            ])
    print(tabulate(ativos, headers, tablefmt="simple_grid")) 

#LISTA TODOS OS CADASTROS - Busca todos cadastrados até o momento
def busca_todos(cadastro):
    '''Busca Todos os cadastros passando somente o parametro "cadastro"'''
    tabela_comp = []
    headers = ['ID','STATUS','NOME','TELEFONE','ENDEREÇO']
    for key, value in cadastro.items():
        tabela_comp.append([
            key,
            cadastro[key]['Status'],
            cadastro[key]['Nome'],
            cadastro[key]['Telefone'],
            cadastro[key]['Endereço']
        ])
    print(tabulate(tabela_comp, headers, tablefmt="simple_grid"))

# LISTA CADASTROS FALSE - busca todos os false
def busca_inativos(cadastro):
    '''Busca todos os cadastros False com o parametro "cadastro"'''
    inativos = []
    headers = ['ID','STATUS','NOME','TELEFONE','ENDEREÇO']
    for key, value in cadastro.items():
        if value['Status'] == False:
            inativos.append([
                key,
                cadastro[key]['Status'],
                cadastro[key]['Nome'],
                cadastro[key]['Telefone'],
                cadastro[key]['Endereço']
            ])
    print(tabulate(inativos, headers, tablefmt="simple_grid")) 
