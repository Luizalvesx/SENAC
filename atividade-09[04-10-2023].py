agenda = []

def adicionar_contato(nome, telefone, email):
    contato = {'Nome': nome, 'Telefone': telefone, 'Email': email}
    agenda.append(contato)
    print(f'Contato {nome} adicionado com sucesso!')

def listar_contatos():
    if agenda:
        for contato in agenda:
            print(f"Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']}")
    else:
        print("A agenda está vazia.")

def pesquisar_contato(nome):
    contatos_encontrados = [contato for contato in agenda if contato['Nome'].lower() == nome.lower()]
    if contatos_encontrados:
        for contato in contatos_encontrados:
            print(f"Contato encontrado: Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']}")
    else:
        print(f"Contato com o nome {nome} não encontrado na agenda.")

while True:
    print("\nMenu:")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Pesquisar Contato")
    print("4. Sair")

    opcao = input("Escolha uma opção (1-4): ")

    if opcao == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(nome, telefone, email)

    elif opcao == '2':
        listar_contatos()

    elif opcao == '3':
        nome_pesquisa = input("Digite o nome do contato para pesquisa: ")
        pesquisar_contato(nome_pesquisa)

    elif opcao == '4':
        print("Saindo da agenda. Até logo!")
        break

    else:
        print("Opção inválida. Escolha novamente.")
