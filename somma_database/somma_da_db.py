class Database:
    def get_valori(self):
        # per ora non lo implementiamo
        raise NotImplementedError


def somma(db: Database):
    a, b = db.get_valori()
    return a + b
