#Função Menu Principal

#Função Adicionar contato
def adicionarContato(lista):
    try:
        nome = input("Digite o nome do contato: ").lower()
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
        for nome, numero in lista.items():
            print(f"Nome: {nome}, Número: {numero}")
        print()

#Função atualizar contatos
def atualizarContatos(lista):
    try:
        print("Para atualizar o nome de um contato, digite '1', para atualizar o número, digite '2'")
        escolha = input("Digite sua escolha ")

        if(escolha == '1'):
            nomeAntigo = input('Digite o nome do contato que deseja atualizar: ').lower()
            if nomeAntigo in lista:
                novoNome = input("Digite o novo nome para atualizar: ").lower()    
                lista[novoNome] = lista.pop(nomeAntigo)
                print("Seu contato foi atualizado!\n")
            else:
                print("Contato não encontrado\n")

        elif(escolha == '2'):
            nome = input("Digite o nome de do contato que deseja atualizar o número: ").lower()
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
        nome = input('Digite o nome do contato que deseja excluir: ').lower()
        if nome in lista:
            lista.pop(nome)
            print("O contato foi excluido com sucesso!\n")
        else:
            print("Contato não encontrado!\n")

    except Exception as e:
        print(f"Erro: {e}\n")

#Função principal:
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
            print("5. Finalizar o programa")
            
            escolha = input("Digite o número da sua escolha: ")

            if(escolha == '1'):
                adicionarContato(lista)
            elif(escolha == '2'):
                excluirContato(lista)
            elif(escolha == '3'):
                atualizarContatos(lista)
            elif(escolha == '4'):
                visualizarContatos(lista)
            elif (escolha == '5'):
                print("Finalizando programa, aqui está sua lista!\n")
                print(lista)
                break
            else:
                print("Escola inválida. Por favor, tente novamente!\n")

    except Exception as e:
        print(f'Erro: {e}!\n')

menuPrincipal()
