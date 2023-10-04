# Números para ordenar
numeros = [34, 7, 22, 107, 89]

# Implementação do algoritmo de ordenação por inserção com apenas um loop for
for i in range(1, len(numeros)):
    for j in range(i, 0, -1):
        if numeros[j] > numeros[j - 1]:
            break
        numeros[j], numeros[j - 1] = numeros[j - 1], numeros[j]

# Imprima a lista ordenada
print("Lista ordenada:", numeros)
