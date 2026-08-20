class Jogador:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.danobonus = 0
        self.agilidadebonus=  0
        self.inventario = []

        self.armas = None
        self.anel = None

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



class Equipamento:
    def __init__(self, nome, dano = 0, valor = 0, agilidade = 0, tipo = None):
        self.nome = nome
        self.dano = dano
        self.valor = valor
        self.agilidade = agilidade
        self.tipo = tipo

quantjogador = int(input("Quantos jogadores teremos na partida? "))

jogadores : list[Jogador] = []

#vida = int(input("Vida dos jogadores: "))
vida = 100

for i in range (quantjogador):
     #nome = str(input(f"Nome do {i + 1}° jogador:  "))
     nome = f"Jogador {i}"
     jogadores.append(Jogador(nome, vida))

jogadoratual = 0
espada = Equipamento ("Espada de Pedra", 5, 8, 0, "arma")
espada2 = Equipamento("Espada de Ferro", 10, 12, 0, "arma")
anel = Equipamento("Anel Mágico", 1, 5, 4, "anel")
anel2 = Equipamento("Anel da agilidade", 1, 7, 50, "anel")
jogadores[0].adicionar_item_inventario(espada)
#jogadores[0].equipar(espada)
jogadores[0].adicionar_item_inventario(espada2)
#jogadores[0].equipar(espada2)
jogadores[0].adicionar_item_inventario(anel)
#jogadores[0].equipar(anel)
jogadores[0].adicionar_item_inventario(anel2)


while True:
    print(f"""
    Vez do jogador: {jogadores[jogadoratual].nome}
    [1] Atacar
    [2] Loja
    [3] Ver inventário
    """)
    opc = int(input("Sua opção: "))

    if opc == 1:
        if quantjogador > 2:

            for i in range(quantjogador):
                if i != jogadoratual:
                     print(f" - [{i}] {jogadores[i].nome}")
            alvo = int(input("Escolha quem você quer atacar: "))

        else:
            for i in range(quantjogador):
                if i != jogadoratual:
                    alvo = i

        print(f"{jogadores[jogadoratual].nome} atacou o {jogadores[alvo].nome}")
        jogadoratual = (jogadoratual + 1) % quantjogador

    if opc == 2:
        pass

    if opc == 3:
        jogadores[jogadoratual].mostrar_inventario()