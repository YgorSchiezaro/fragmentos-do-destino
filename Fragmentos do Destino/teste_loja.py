from equipamento import Equipamento
from loja import Loja
from rich.console import Console
from rich.table import Table
from rich import box
console = Console()


loja = Loja()

espada_pedra = Equipamento(
    nome="Espada de Pedra",
    dano=5,
    valor=8,
    agilidade=0,
    tipo="arma",
)

anel_magico = Equipamento(
    nome="Anel Mágico",
    dano=1,
    valor=5,
    agilidade=4,
    tipo="anel",
)

loja.cadastrar_equipamento(espada_pedra)
loja.cadastrar_equipamento(anel_magico)

loja.listar_equipamentos()

from jogador import Jogador

jogador_teste = Jogador("Comprador Teste", 10)
jogador_teste.adicionar_moedas(20)

loja.comprar_equipamentos(jogador_teste)

print("\nItens do jogador:")

for item in jogador_teste.inventario:
    print(f"- {item.nome}")

print(f"Saldo restante: {jogador_teste.moedas} moedas")