from jogador import Jogador
from equipamento import Equipamento
from combate import Combate
from partida import Partida
from entrada import ler_inteiro
from loja import Loja
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich import box, status

console = Console()


def criar_loja() -> Loja:
    loja = Loja()

    equipamentos = [
        Equipamento("Espada de Pedra", 5, 8, 0, "arma"),
        Equipamento("Espada de Ferro", 10, 12, 0, "arma"),
        Equipamento("Anel Mágico", 1, 5, 4, "anel"),
        Equipamento("Anel da agilidade", 1, 7, 50, "anel"),
    ]

    for equipamento in equipamentos:
        loja.cadastrar_equipamento(equipamento)
    return loja


def mostrar_menu(jogador: Jogador) -> None:
    status = Table.grid(expand=True)
    status.add_column(justify="center")


    status.add_row(
        f"[bold cyan]🧙 {jogador.nome}[/bold cyan]",
        f"[bold red]❤️ {jogador.vida} HP[/bold red]",
        f"[bold yellow]💰 {jogador.moedas} Moedas[/bold yellow]",
    )
    opcoes = Table(
        show_header=True,
        header_style="bold magenta",
        border_style="bright_blue",
        box = box.DOUBLE_EDGE,
        expand = True,
    )

    opcoes.add_column("Opção", justify="center", width = 4)
    opcoes.add_column("Ação", justify="center")
    opcoes.add_row("[cyan]0[/cyan]", "🚪 Sair da partida")
    opcoes.add_row("[cyan]1[/cyan]", "⚔️ Atacar")
    opcoes.add_row("[cyan]2[/cyan]", "🛒 Visitar loja")
    opcoes.add_row("[cyan]3[/cyan]", "📦 Abrir inventário")

    painel = Panel(
        Group(status, opcoes),
        title="[bold magenta] ✨ FRAGMENTOS DO DESTINO ✨ [/bold magenta]",
        subtitle="[dim]Escolha sua próxima ação[/dim]",
        border_style="bright_magenta",
        box = box.DOUBLE,
    )

    console.print()
    console.print(painel)

def main() -> None:
    quantjogador = ler_inteiro(
        "Quantos jogadores teremos na partida? ",
        minimo=2,
    )
    jogadores = Partida.registrar_jogadores(
        quantjogador=quantjogador,
        vida=100,

    )
    partida = Partida(jogadores)
    loja = criar_loja()
    jogador_atual = jogadores[0]



    while True:
        partida.verificar_mortos()
        if partida.fim_partida():
            break

        mostrar_menu(jogador_atual)

        opc = ler_inteiro("Sua opção: ", opcoes={0, 1, 2, 3})

        if opc == 0:
            print("Partida encerrada.")
            break

        if opc == 1:
            combate = Combate(jog=jogador_atual, jogadores=jogadores)
            combate.atacar()
            partida.verificar_mortos()

            if len(jogadores) > 1:
                jogador_atual = partida.proximo_jogador(jogador_atual)
        elif opc == 2:
            loja.comprar_equipamentos(jogador_atual)

        elif opc == 3:
            jogador_atual.mostrar_inventario()



if __name__ == "__main__":
    main()
