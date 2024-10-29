
def main():
    # Calcular limite para o infinito negativo
    print("Limite (-inf):")
    for i in range(0, -31, -1):
        # Valor de x se aproximando de -inf indo de 0 até -1
        x = i
        print(f"f({x}) =", func(x))
    """ Tende a -1 """

# sqrt(x^2 + 1)/(x + 1)
def func(x):
    if x == -1:
        return None
    return ((x ** 2 + 1) ** 0.5)/(x + 1)

# Inicializa o programa
main()