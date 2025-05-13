def somma(a, b):
    return a + b


def somma_pari(a, b):
    if a + b % 2 == 0:
        return somma(a, b)
