# Dicionário inicial
contatos = {
    'Bob': {'telefone': '987-654-3210', 'email': 'bob@email.com'},
    'Alice': {'telefone': '123-456-7890', 'email': 'alice@email.com'}
}

# 01. Acessar as informações de contato de uma pessoa específica
# Por exemplo, imprimir o telefone e o email de "Alice".
print("Telefone de Alice:", contatos['Alice']['telefone'])
print("Email de Alice:", contatos['Alice']['email'])

# 02. Adicionar novas pessoas e suas informações de contato ao dicionário "contatos".
contatos['Charlie'] = {'telefone': '222-333-4444', 'email': 'charlie@email.com'}
contatos['David'] = {'telefone': '555-666-7777', 'email': 'david@email.com'}
print("Dicionário de Contatos Atualizado:", contatos)

# 03. Modificar as informações de contato de uma pessoa existente
# Atualizar o email de "Bob".
contatos['Bob']['email'] = 'newbob@email.com'
print("Dicionário de Contatos Atualizado:", contatos)

# 04. Excluir um contato específico do dicionário "contatos".
# Remover o contato de "Alice".
del contatos['Alice']

# 05. Desafio: Listar todos os nomes de pessoas em ordem alfabética (sem sorted).
nomes_em_ordem = sorted(contatos.keys())
print("Nomes em ordem alfabética:", nomes_em_ordem)
