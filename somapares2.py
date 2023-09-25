def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

n = int(input("Digite um número inteiro para calcular o fatorial: "))
resultado = fatorial(n)
print(f"O fatorial de {n} é {resultado}")
