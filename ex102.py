def fatorial(n, show=False):
    """
    → Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o cálculo.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal
n = int(input("Qual o valor que você quer fatorizar? "))
print(fatorial(n, show=True))
help(fatorial)
