#Função Adicionar contato
def adicionarContato(lista):
    try:
        nome = input("Digite o nome do contato: ").title()
        numero = int(input("Digite o numero do contato: "))
        lista[nome] = numero
        print("Contato adicionado com sucesso!\n")
    except ValueError:
        print('Erro: Por favor, insira um número válido para o contato!.\n')
    except Exception as e:
        print(f"Erro: {e}\n")

#Função visualizar lista de contatos
def visualizarContatos(lista):
    if not lista:
        print("Sua lista está vazia! Vamos adicionar alguns contatos?\n")
    else:    
        print("Lista de contatos:")
        ordenarContatos(lista)

#Função atualizar contatos
def atualizarContatos(lista):
    try:
        print("Para atualizar o nome de um contato, digite '1', para atualizar o número, digite '2'")
        escolha = input("Digite sua escolha ")

        if(escolha == '1'):
            nomeAntigo = input('Digite o nome do contato que deseja atualizar: ').title()
            if nomeAntigo in lista:
                novoNome = input("Digite o novo nome para atualizar: ").title()    
                lista[novoNome] = lista.pop(nomeAntigo)
                print("Seu contato foi atualizado!\n")
            else:
                print("Contato não encontrado\n")

        elif(escolha == '2'):
            nome = input("Digite o nome de do contato que deseja atualizar o número: ").title()
            if nome in lista:
                novoNumero = int(input("Digite o novo número: "))
                lista[nome] = novoNumero
                print("Seu contato foi atualizado!\n")
            else:
                print("Contato não encontrado!\n")

        else:
            print('Opção inválida, tente novamente!\n')

    except ValueError:
        print('Erro: Por favor, insira um número válido para o número de telefone\n')
    except Exception as e:
        print(f"Erro: {e}\n")

#Função excluir contato:
def excluirContato(lista):
    try:
        nome = input('Digite o nome do contato que deseja excluir: ').title()
        if nome in lista:
            lista.pop(nome)
            print("O contato foi excluido com sucesso!\n")
        else:
            print("Contato não encontrado!\n")

    except Exception as e:
        print(f"Erro: {e}\n")

#Função Buscar Contatos:
def buscarContatos(lista):
    escolha = input("Digite o nome: ")
    resultado = []

    for nome, numero in lista.items():
        if escolha.title() in nome.title():
            resultado.append((nome, numero))

    if resultado:
        print("Aqui está o resultado da busca:")
        for nome, numero in resultado:
            print(f"Nome: {nome}, Número: {numero}")
    
    else:
        print("Nenhum contato foi encontrado!")

#Função ordenar contatos:
def ordenarContatos(lista):
    listaOrdenada = sorted(lista.keys())
    for contato in listaOrdenada:
        numero = lista[contato]
        print(f"Nome: {contato}, Número: {numero}\n")

#Função menu principal:
def menuPrincipal():
    try:
        lista = {}
        print("Bem vindo a sua nova lista de contatos!\n")

        while True:
            print("O que deseja fazer?")
            print("1. Adicionar um contato")
            print("2. Excluir um contato")
            print("3. Atualizar um contato")
            print("4. Visualizar lista de contatos")
            print("5. Buscar contatos")
            print("6. Finalizar o programa")
            
            escolha = input("Digite o número da sua escolha: ")

            if(escolha == '1'):
                adicionarContato(lista)
            elif(escolha == '2'):
                excluirContato(lista)
            elif(escolha == '3'):
                atualizarContatos(lista)
            elif(escolha == '4'):
                visualizarContatos(lista)
            elif(escolha == '5'):
                buscarContatos(lista)
            elif (escolha == '6'):
                print("Finalizando programa, aqui está sua lista!\n")
                ordenarContatos(lista)
                break
            else:
                print("Escola inválida. Por favor, tente novamente!\n")

    except Exception as e:
        print(f'Erro: {e}!\n')

menuPrincipal()