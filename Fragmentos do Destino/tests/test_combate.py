import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from combate import Combate
from jogador import Jogador


class TestCombate(unittest.TestCase):
    def test_nao_permite_atacar_a_si_mesmo_ou_indice_invalido(self):
        jogador_1 = Jogador("Jogador 1", 10)
        jogador_2 = Jogador("Jogador 2", 10)
        jogador_3 = Jogador("Jogador 3", 10)
        combate = Combate(jogador_2, [jogador_1, jogador_2, jogador_3])

        entradas = ["1", "texto", "5", "2"]
        with patch("builtins.input", side_effect=entradas):
            with redirect_stdout(io.StringIO()):
                alvo = combate.escolher_alvo()

        self.assertIs(alvo, jogador_3)

    def test_ataque_causa_dano_no_alvo(self):
        atacante = Jogador("Atacante", 10)
        alvo = Jogador("Alvo", 10)
        atacante.dado20 = lambda: 15
        atacante.dado10 = lambda: 3
        combate = Combate(atacante, [atacante, alvo])

        with redirect_stdout(io.StringIO()):
            dano = combate.atacar()

        self.assertEqual(dano, 3)
        self.assertEqual(alvo.vida, 7)

    def test_ataque_que_falha_nao_causa_dano(self):
        atacante = Jogador("Atacante", 10)
        alvo = Jogador("Alvo", 10)
        atacante.dado20 = lambda: 10
        combate = Combate(atacante, [atacante, alvo])

        with redirect_stdout(io.StringIO()):
            dano = combate.atacar()

        self.assertEqual(dano, 0)
        self.assertEqual(alvo.vida, 10)


if __name__ == "__main__":
    unittest.main()
