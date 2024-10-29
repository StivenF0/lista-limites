
def main():
    # Calcular limite pela direita
    print("Limite pela direita (3+):")
    for i in range(15):
        # Valor de x pela direita se aproximando de 3
        x = 3 + (1 / (i+1))
        print(f"f({x:.03f}) =", func(x))
    """ Tende a 3 """
    
    # Calcular limite pela esquerda
    print("Limite pela esquerda (3-):")
    for i in range(15):
        # Valor de x pela esquerda se aproximando de 3
        x = 3 - (1 / (i+1))
        print(f"f({x:.03f}) =", func(x))
    """ Tende a -1 """

    """ O limite bilateral não existe, pois os laterais não tendem ao mesmo valor. """

# funcao f:
# se x > 3 então y = 3
# se x = 3 então y = 1
# se x < 3 então y = -1
def func(x):
    if x > 3:
        return 3
    if x == 3:
        return 1
    return -1

# Inicializar programa
main()