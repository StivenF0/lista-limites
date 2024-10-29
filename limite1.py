
def main():
    # Calcular limite pela direita
    print("Limite pela direita (0+):")
    for i in range(15):
        # Valor de x pela direita se aproximando de 0
        x = (1 / (i+1))
        print(f"f({x:.03f}) =", func(x))
    """ Tende ao infinito negativo """
    
    # Calcular limite pela esquerda
    print("Limite pela esquerda (0-):")
    for i in range(15):
        # Valor de x pela esquerda se aproximando de 0
        x = -(1 / (i+1))
        print(f"f({x:.03f}) =", func(x))
    """ Tende ao infinito positivo """

    """ O limite bilateral não existe, pois os laterais não tendem ao mesmo valor. """

# f(x) = 1 - 1/x
def func(x):
    if x != 0:
        return 1 - 1/x
    return None

# Iniciar programa
main()