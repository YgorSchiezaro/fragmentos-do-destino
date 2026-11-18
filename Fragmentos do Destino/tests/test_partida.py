import io
import unittest
from contextlib import redirect_stdout

from jogador import Jogador
from partida import Partida


class TestPartida(unittest.TestCase):
    def test_exige_pelo_menos_dois_jogadores(self):
        with self.assertRaises(ValueError):
            Partida.registrar_jogadores(1, vida=10)

    def test_remove_mortos_e_preserva_os_vivos(self):
        jogador_1 = Jogador("Jogador 1", 10)
        jogador_2 = Jogador("Jogador 2", 0)
        partida = Partida([jogador_1, jogador_2])

        with redirect_stdout(io.StringIO()):
            mortos = partida.verificar_mortos()

        self.assertEqual(mortos, [jogador_2])
        self.assertEqual(partida.jogadores, [jogador_1])
        self.assertEqual(partida.mortos, [jogador_2])

    def test_proximo_turno_continua_correto_apos_remocao(self):
        jogador_1 = Jogador("Jogador 1", 0)
        jogador_2 = Jogador("Jogador 2", 10)
        jogador_3 = Jogador("Jogador 3", 10)
        partida = Partida([jogador_1, jogador_2, jogador_3])

        with redirect_stdout(io.StringIO()):
            partida.verificar_mortos()

        self.assertIs(partida.proximo_jogador(jogador_2), jogador_3)

    def test_partida_sem_jogadores_termina_sem_erro(self):
        partida = Partida([])
        saida = io.StringIO()

        with redirect_stdout(saida):
            terminou = partida.fim_partida()

        self.assertTrue(terminou)
        self.assertIn("Todo mundo morreu", saida.getvalue())


if __name__ == "__main__":
    unittest.main()
