from random import randint
from time import sleep
from equipamento import Equipamento

class Jogador:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.danobonus = 0
        self.agilidadebonus=  0
        self.inventario = []

        self.armas: Equipamento = None
        self.anel = None

    def dado20(self):
        print("ROLANDO DADO DE AGILIDADE")
        sleep(0.5)
        dado20 = randint(10, 20)
        print(dado20)
        return dado20

    def dado10(self):
        print("ROLANDO DADO DE ATAQUE")
        sleep(0.5)
        dado10 = randint(1, 10)
        print(dado10)
        return dado10

    def danototal(self, dado10, dado20):
        danotot = dado10
        if self.danobonus > 0:
            print(f" + {self.danobonus} de bônus")
            danotot += self.danobonus
        if self.armas and self.armas.dano > 0:
            danotot += self.armas.dano
            print(f" + {self.armas.dano} de armas")

        if dado20 >= 20:
            print("GANHOU UM BÔNUS. ESPECIAL ATIVADO!!!")
            sleep(0.3)
            danotot *= 2
        return danotot


    def adicionar_item_inventario(self, item):
        print(f"- {item.nome} foi adicionado no inventário")
        self.inventario.append(item)

    def mostrar_inventario(self):

        if not self.inventario:
            print("Inventario vazio")
            return
        opc = 0
        fim = len(self.inventario)
        while opc != fim:
            for i, item in enumerate(self.inventario):
                print(f"- [{i}] {item.nome} - Dano: {item.dano} - Agilidade: {item.agilidade} - Tipo: {item.tipo}")
            print(f" - [{fim}] Saída")

            if self.armas:
                print(f"Arma Equipada: {self.armas.nome}")
            if self.anel:
                print(f"Anel Equipado: {self.anel.nome}")
            opc = int (input("> "))
            if opc == fim or opc == "fim":
                return
            if self.inventario[opc].tipo == 'arma' or self.inventario[opc].tipo == 'anel':
                self.equipar(self.inventario[opc])


    def equipar(self, item):
        if item not in self.inventario:
            print(f"O item {item.nome} não está no inventário")
            return
        if item.tipo == 'arma':
            if self.armas:
                print(f"Desequipando {self.armas.nome}")
            self.armas = item
        elif item.tipo == 'anel':
            if self.anel:
                print(f"Desequipando {item.nome}")
            self.anel = item
        print(f"{self.nome} equipou {item.nome}")
