# Função para calcular uma função de primeiro grau f(x) = ax + b
def calcular_funcao_afim(x, a, b):
    resultado = a * x + b
    return resultado

# Função principal
def main():
    print("Calculadora de Função de Primeiro Grau (f(x) = ax + b)")
    
    # Solicitar ao usuário os valores de 'a', 'b' e 'x'
    a = float(input("Digite o valor de 'a': "))
    b = float(input("Digite o valor de 'b': "))
    x = float(input("Digite o valor de 'x': "))
    
    # Calcular o valor da função
    resultado = calcular_funcao_afim(x, a, b)
    
    # Exibir o resultado
    print("O valor de f(x) para x = {} é: {}".format(x, resultado))

if __name__ == "__main__":
    main()
