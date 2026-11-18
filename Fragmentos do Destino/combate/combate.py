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

        return self.ialvo

    def atacar(self) -> int:
        alvo = self.escolher_alvo()
        print(f"\n{self.jog.nome} atacou {alvo.nome}!")
        print("ROLANDO DADO DE AGILIDADE")
        dado20_base = self.jog.dado20()
        bonus_agilidade = self.jog.bonus_agilidade()
        dado20 = dado20_base + bonus_agilidade
        print(f"Resultado do dado : {dado20_base}")

        if bonus_agilidade > 0:
            print(f"Bônus de agilidade: +{bonus_agilidade}")

        print(f"Agilidade total: {dado20}")
        
        if dado20 <= 10:
            print("O ataque errou!")
            return 0

        print("ROLANDO DADO DE ATAQUE")
        dado10 = self.jog.dado10()
        print(f"Resultado: {dado10}")

        print('ROLANDO DADO DA SORTE')
        dado_sorte = self.jog.dado_sorte()
        print(f"Resultado: {dado_sorte}")

        dano_total = self.jog.danototal(dado10, dado20, dado_sorte)

        if dado20 >= 20 or dado_sorte == 10:
            print('GANHOU UM BÔNUS, ESPECIAL ATIVADO!!!')

        alvo.vida -= dano_total

        print(f'{alvo.nome} perdeu {dano_total} de HP!')
        return dano_total