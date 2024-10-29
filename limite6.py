
def main():
    # Calcular limite para o infinito positivo
    print("Limite (+inf):")
    for i in range(1, 30 + 1):
        # Valor de x se aproximando de +inf
        x = i
        print(f"f({x}) =", func(x))
    """ Tende a 0 """

# (t + 1)/(t^2 + 1)
def func(t):
    return (t + 1)/(t ** 2 + 1)

# Inicializa o programa
main()