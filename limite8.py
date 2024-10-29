from math import sin


def main():
    # Calcular limite pela direita
    print("Limite pela direita (0+):")
    for i in range(15):
        # Valor de x pela direita se aproximando de 0
        x = (1 / (i+1))
        print(f"f({x:.03f}) =", func(x))
    """ Tende a 1.333 """
    
    # Calcular limite pela esquerda
    print("Limite pela esquerda (0-):")
    for i in range(15):
        # Valor de x pela esquerda se aproximando de 0
        x = -(1 / (i+1))
        print(f"f({x:.03f}) =", func(x))
    """ Tende a 1.333 """

    """ O limite bilateral é 1.333, pois os laterais existem. """

# sen(4x)/3x
def func(x):
    if x == 0:
        return None
    return sin(4 * x)/(3 * x)

# Inicializando programa
main()