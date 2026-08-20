from jogador import Jogador, jogador


class Partida:
    def __init__(self, jogadores:Jogador):
        self.jogadores = jogadores
        self.mortos = []

    @classmethod
    def registrar_jogadores(cls, quantjogador, vida):
        jogadores = []
        for i in range(quantjogador):
            # nome = str(input(f"Nome do {i + 1}° jogador:  "))
            nome = f"Jogador {i + 1}"
            jogadores.append(Jogador(nome, vida))
        return jogadores

    def verificar_mortos(self):
        for jogador in self.jogadores[:]:
            if jogador.vida <= 0:
                print(f"{jogador.nome} morreu")
                self.mortos.append(jogador)
                self.jogadores.remove(jogador)
    def listar_mortos(self):
        print("Vivos:")
        for jog in self.jogadores:
            print(jog.nome)
        if self.mortos:
            print(f"Lista de mortos: ")
            for morto in self.mortos:
                print(morto.nome)
    def fim_partida(self):
        if len(self.jogadores) <= 1:
            if self.jogadores[0].vida >= 1:
                campeao = self.jogadores[0]
                print(f"{campeao.nome} venceu a partida")
            else:
                print("Todo mundo morreu")
            return True
        return False