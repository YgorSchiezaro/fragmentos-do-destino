from jogador import Jogador
from equipamento import Equipamento
from combate import Combate
from partida import Partida

quantjogador = int(input("Quantos jogadores teremos na partida? "))

jogadores : list[Jogador] = Partida.registrar_jogadores(quantjogador = quantjogador, vida= 10)

partida = Partida(jogadores)
partida.verificar_mortos()
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

    partida.verificar_mortos()

    if partida.fim_partida():
        break

    if jogadoratual >= len(jogadores):
        jogadoratual = 0

    print(f"""
    Vez do jogador: {jogadores[jogadoratual].nome} ---- HP: {jogadores[jogadoratual].vida}
    [1] Atacar
    [2] Loja
    [3] Ver inventário
    """)
    opc = int(input("Sua opção: "))

    if opc == 1:

        combate = Combate(jog = jogadores[jogadoratual], jogadores = jogadores, indice= jogadoratual)
        combate.atacar()

        jogadoratual = (jogadoratual + 1) % len(jogadores)

    if opc == 2:
        pass

    if opc == 3:
        jogadores[jogadoratual].mostrar_inventario()