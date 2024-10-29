
def main():
    # Calcular limite para o infinito positivo
    print("Limite (+inf):")
    for i in range(1, 31):
        # Valor de x aproximando de +inf
        x = i * 10000
        print(f"f({x}) =", func(x))
    """ Tende a e^10, que é aproximadamente 22026.465 """
    
# (1 + 10/x)^x
def func(x):
    if x == 0:
        return None
    return (1 + 10/x) ** x

# Inicializa programa
main()