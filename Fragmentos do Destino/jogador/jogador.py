from random import randint
from time import sleep
from equipamento import Equipamento
from entrada import ler_inteiro


class Jogador:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.danobonus = 0
        self.agilidadebonus = 0
        self.inventario = []
        self.moedas = 0
        self.vida_maxima = vida

        self.armas: Equipamento | None = None
        self.anel: Equipamento | None = None

    def dado20(self):
        print("ROLANDO DADO DE AGILIDADE")
        sleep(0.5)
        dado20 = randint(1, 20)
        print(dado20)
        return dado20

    def dado10(self):
        print("ROLANDO DADO DE ATAQUE")
        sleep(0.5)
        dado10 = randint(1, 10)
        print(dado10)
        return dado10

    def dado_sorte(self):
        print("ROLANDO DADO DA SORTE")
        sleep(0.5)

        sorte = randint(1, 10)
        print(f"Resultado do seu dado da sorte: {sorte}")
        return sorte


    def danototal(self, dado10, dado20, dado_sorte):
        danotot = dado10
        if self.danobonus > 0:
            danotot += self.danobonus

        if self.armas and self.armas.dano > 0:
            danotot += self.armas.dano
            print(f" + {self.armas.dano} de armas")

        if dado20 >= 20 or dado_sorte == 10:
            print("GANHOU UM BÔNUS. ESPECIAL ATIVADO!!!")
            sleep(0.3)
            danotot *= 2
        return danotot

    def restaurar_vidas(self):
        self.vida = self.vida_maxima
        print(f"❤️ A vida de {self.nome} foi restaurada para {self.vida}.")

    def adicionar_item_inventario(self, item):
        print(f"\n- {item.nome} foi adicionado no inventário")
        self.inventario.append(item)

    def mostrar_inventario(self):

        if not self.inventario:
            print("Inventario vazio")
            return
        fim = len(self.inventario)
        while True:
            for i, item in enumerate(self.inventario):
                print(f"- [{i}] {item.nome} - Dano: {item.dano} - Agilidade: {item.agilidade} - Tipo: {item.tipo}")
            print(f" - [{fim}] Saída")

            if self.armas:
                print(f"Arma Equipada: {self.armas.nome}")
            if self.anel:
                print(f"Anel Equipado: {self.anel.nome}")
            opc = ler_inteiro("> ", minimo=0, maximo=fim)
            if opc == fim:
                return

            item = self.inventario[opc]
            if item.tipo in {"arma", "anel"}:
                self.equipar(item)


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
                print(f"Desequipando {self.anel.nome}")
            self.anel = item
        print(f"{self.nome} equipou {item.nome}")

    def adicionar_moedas(self, quantidade):
        if quantidade <= 0:
            print("Você esta pobre. A quantidade de moedas deve ser positiva.")
            return
        self.moedas += quantidade
        print(f"{self.nome} recebeu {quantidade} de moedas.")
        print(f"Saldo atual: {self.moedas}")

    def gastar_moedas(self, quantidade):
        if quantidade <= 0:
            print("Valor de compra inválido.")
            return False
        if self.moedas < quantidade:
            print(f"{self.nome} não possui moedas suficientes. Vai jogar para tentar ter dinheiro!!")
            return False
        self.moedas -= quantidade
        print(f"Compra realizada. Saldo Atual: {self.moedas} moedas.")
        return True

