import unittest
from unittest.mock import MagicMock
from somma_da_db import somma


class TestConMockDatabase(unittest.TestCase):
    def test_somma_mock_db(self):
        # Crea un mock del database
        mock_db = MagicMock()
        mock_db.get_valori.return_value = (3, 5)

        risultato = somma(mock_db)

        self.assertEqual(risultato, 8)


if __name__ == "__main__":
    unittest.main()
