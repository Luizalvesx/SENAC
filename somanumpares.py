def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)

n = int(input("Digite um número inteiro para calcular o fatorial: "))
resultado = fatorial(n)
print(f"O fatorial de {n} é {resultado}")
print("Ola mundo")
