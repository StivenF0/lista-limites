
def main():
    # Calcular limite pela direita
    print("Limite pela direita (1+):")
    for i in range(15):
        # Valor de x pela direita se aproximando de 1
        x = 1 + (1 / (i+1))
        print(f"f({x:.03f}) =", func(x))
    """ Tende a 2 """
    
    # Calcular limite pela esquerda
    print("Limite pela esquerda (1-):")
    for i in range(15):
        # Valor de x pela esquerda se aproximando de 1
        x = 1 - (1 / (i+1))
        print(f"f({x:.03f}) =", func(x))
    """ Tende a 2 """

    """ O limite bilateral é 2, pois os laterais existem e são iguais. """

# f(x) = (x^2 - 1)/(x - 1)
def func(x):
    if x == 1:
        return None
    return (x ** 2 - 1)/(x - 1)

main()