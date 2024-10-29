
def main():
    # Calcular limite pela direita
    print("Limite pela direita (2+):")
    for i in range(15):
        # Valor de x pela direita se aproximando de 2
        x = 2 + (1 / (i+1))
        print(f"f({x:.03f}) =", func(x))
    """ Tende a 1.25 """
    
    # Calcular limite pela esquerda
    print("Limite pela esquerda (2-):")
    for i in range(15):
        # Valor de x pela esquerda se aproximando de 2
        x = 2 - (1 / (i+1))
        print(f"f({x:.03f}) =", func(x))
    """ Tende a 1.25 """

    """ O limite bilateral é 1.25, pois os laterais existem e são iguais. """

# f(t) = (t + 3)/(t + 2)
def func(t):
    if t == -2:
        return None
    return (t + 3)/(t + 2)

# Inicializa o programa
main()