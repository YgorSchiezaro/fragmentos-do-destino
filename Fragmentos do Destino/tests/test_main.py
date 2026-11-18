import importlib.util
import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


CAMINHO_MAIN = Path(__file__).resolve().parents[1] / "__main__.py"
ESPECIFICACAO = importlib.util.spec_from_file_location("jogo_main", CAMINHO_MAIN)
MODULO_MAIN = importlib.util.module_from_spec(ESPECIFICACAO)
ESPECIFICACAO.loader.exec_module(MODULO_MAIN)


class TestMain(unittest.TestCase):
    def test_jogo_inicia_e_permite_sair(self):
        entradas = ["texto", "1", "2", "0"]
        saida = io.StringIO()

        with patch("builtins.input", side_effect=entradas):
            with redirect_stdout(saida):
                MODULO_MAIN.main()

        texto = saida.getvalue()
        self.assertIn("Digite um número inteiro.", texto)
        self.assertIn("Digite um número maior ou igual a 2.", texto)
        self.assertIn("Partida encerrada.", texto)


if __name__ == "__main__":
    unittest.main()
