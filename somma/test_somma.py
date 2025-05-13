from somma import somma


def test_somma_2_3():
    assert somma(2, 3) == 5


def test_somma_4_3():
    assert somma(4, 3) == 7


def test_somma_sbagliata():
    assert somma(4, 2) != 7
