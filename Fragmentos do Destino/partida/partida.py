from jogador import Jogador


class Partida:
    def __init__(self, jogadores: list[Jogador]):
        self.jogadores = jogadores
        self.mortos: list[Jogador] = []

    @classmethod
    def registrar_jogadores(cls, quantjogador: int, vida: int) -> list[Jogador]:
        if quantjogador < 2:
            raise ValueError("A partida precisa de pelo menos dois jogadores.")

        jogadores = []
        for i in range(quantjogador):
            # nome = str(input(f"Nome do {i + 1}° jogador:  "))
            nome = f"Jogador {i + 1}"
            jogadores.append(Jogador(nome, vida))
        return jogadores

    def verificar_mortos(self) -> list[Jogador]:
        mortos_neste_turno = []
        for jogador in self.jogadores[:]:
            if jogador.vida <= 0:
                print(f"{jogador.nome} morreu")
                self.mortos.append(jogador)
                self.jogadores.remove(jogador)
                mortos_neste_turno.append(jogador)
        return mortos_neste_turno

    def proximo_jogador(self, jogador_atual: Jogador) -> Jogador:
        if not self.jogadores:
            raise ValueError("Não há jogadores vivos na partida.")
        if jogador_atual not in self.jogadores:
            raise ValueError("O jogador atual não está mais na partida.")

        indice_atual = self.jogadores.index(jogador_atual)
        proximo_indice = (indice_atual + 1) % len(self.jogadores)
        return self.jogadores[proximo_indice]

    def listar_mortos(self):
        print("Vivos:")
        for jog in self.jogadores:
            print(jog.nome)
        if self.mortos:
            print("Lista de mortos:")
            for morto in self.mortos:
                print(morto.nome)

    def fim_partida(self):
        if not self.jogadores:
            print("Todo mundo morreu")
            return True

        if len(self.jogadores) == 1:
            campeao = self.jogadores[0]
            print(f"{campeao.nome} venceu a partida")
            return True

        return False
