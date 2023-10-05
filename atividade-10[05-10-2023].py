def soma_recursiva(seq):
    # Caso base: se a sequência estiver vazia, a soma é 0
    if not seq:
        return 0
    else:
        # A soma é o primeiro elemento da sequência mais a soma dos restantes
        return seq[0] + soma_recursiva(seq[1:])

# Exemplo de uso
minha_sequencia = [1, 2, 3, 4, 5]
resultado = soma_recursiva(minha_sequencia)
print(f"A soma da sequência {minha_sequencia} é {resultado}")
