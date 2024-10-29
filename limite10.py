
def main():
    # Calcular limite pela direita
    print("Limite pela direita (2+):")
    for i in range(15):
        # Valor de x pela direita se aproximando de 2
        x = 2 + (1 / (i + 1))
        print(f"f({x:.03f}) =", func(x))
    """ Tende a 2.302 ou ln(10) """
    
    # Calcular limite pela esquerda
    print("Limite pela esquerda (2-):")
    for i in range(15):
        # Valor de x pela esquerda se aproximando de 2
        x = 2 - (1 / (i + 1))
        print(f"f({x:.03f}) =", func(x))
    """ Tende a 2.302 ou ln(10) """

    """ O limite bilateral é 2.302 ou ln(10), pois os laterais existem e são iguais. """

# (10^(x - 2) - 1)/(x - 2)
def func(x):
    if x == 2:
        return None
    return ((10 ** (x - 2)) - 1)/(x - 2)

# Inicializa o programa
main()