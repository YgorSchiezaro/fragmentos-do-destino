from jogador import Jogador

class Combate:
    def __init__(self, jog, jogadores, indice):
        self.jog: Jogador = jog
        self.jogadores = jogadores
        self.indice = indice # indice do jogador atual
        self.qj = len(self.jogadores)
        self.ialvo: Jogador = None #jogador que será atacado

    def escolher_alvo(self):
        if self.qj > 2:
            for i in range(self.qj):
                if i != self.indice:
                     print(f" - [{i}] {self.jogadores[i].nome}")
            ialvo = int(input("Escolha quem você quer atacar: "))

        else:
            for i in range(self.qj):
                if i != self.indice:
                    ialvo = i
        self.ialvo = self.jogadores[ialvo]
        print(f"{self.jog.nome } atacou o {self.ialvo.nome}")

    def atacar(self):
        self.escolher_alvo()
        dado20 = self.jog.dado20()
        if dado20 > 10:
            dado10 = self.jog.dado10()
            danotot = self.jog.danototal(dado10, dado20)
            self.ialvo.vida -= danotot
            print(f"{self.ialvo.nome} perdeu {danotot} de HP ")
        else:
            print("Errou o dano!!")

