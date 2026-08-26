from jogador import Jogador
from entrada import ler_inteiro


class Combate:
    def __init__(self, jog: Jogador, jogadores: list[Jogador]):
        if jog not in jogadores:
            raise ValueError("O jogador atacante não está na partida.")

        self.jog: Jogador = jog
        self.jogadores = jogadores
        self.ialvo: Jogador | None = None

    def escolher_alvo(self) -> Jogador:
        alvos = {
            indice: jogador
            for indice, jogador in enumerate(self.jogadores)
            if jogador is not self.jog
        }

        if not alvos:
            raise ValueError("Não há outro jogador disponível para atacar.")

        if len(alvos) == 1:
            self.ialvo = next(iter(alvos.values()))
        else:
            print("Escolha o alvo:e")
            for indice, jogador in alvos.items():
                print(f" - [{indice}] {jogador.nome}")

            indice_alvo = ler_inteiro(
                "Escolha quem você quer atacar: ",
                opcoes=set(alvos),
            )
            self.ialvo = alvos[indice_alvo]

        print(f"{self.jog.nome} atacou {self.ialvo.nome}")
        return self.ialvo

    def atacar(self) -> int:
        alvo = self.escolher_alvo()
        dado20 = self.jog.dado20()
        if dado20 > 10:
            dado10 = self.jog.dado10()
            dado_sorte = self.jog.dado_sorte()
            danotot = self.jog.danototal(dado10, dado20, dado_sorte)
            alvo.vida -= danotot
            print(f"{alvo.nome} perdeu {danotot} de HP")
            return danotot

        print("O ataque errou!")
        return 0
