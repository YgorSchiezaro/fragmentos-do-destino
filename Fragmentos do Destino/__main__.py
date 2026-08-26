from jogador import Jogador
from equipamento import Equipamento
from combate import Combate
from partida import Partida
from entrada import ler_inteiro
from loja import Loja
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich import box

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

    todos_jogadores = Partida.registrar_jogadores(
        quantjogador=quantjogador,
        vida=100,
    )

    loja = criar_loja()

    #SE QUISER COMEÇAR COM MOEDAS, ATIVE O CÓDIGO ABAIXO
    #SE QUISER QUE UM DETERMINADO JOGADOR COMECE COM MOEDA COMECE ASSIM:
    #todos_jogadores[0]
    todos_jogadores[0].adicionar_moedas(20)

    while True:
        jogadores = todos_jogadores.copy()
        partida = Partida(jogadores)
        jogador_atual = jogadores[0]

        while True:
            partida.verificar_mortos()

            if partida.fim_partida():
                if len(jogadores) == 1:
                    campeao = jogadores[0]

                    console.print(
                        f"\n[bold yellow]"
                        f"🏆 {campeao.nome} venceu a partida!"
                        f"[/bold yellow]"
                    )

                    premio = 8

                    console.print(
                        "\n[bold cyan]"
                        "🎲 Dado da sorte da recompensa!"
                        "[/bold cyan]"
                    )

                    sorte_premio = campeao.dado_sorte()

                    if sorte_premio == 10:
                        premio *= 2

                        console.print(
                            "[bold bright_yellow]"
                            "✨ SORTE MÁXIMA! RECOMPENSA X2!"
                            "[/bold bright_yellow]"
                        )

                    campeao.adicionar_moedas(premio)

                break

            mostrar_menu(jogador_atual)

            opc = ler_inteiro(
                "Sua opção: ",
                opcoes={0, 1, 2, 3},
            )

            if opc == 0:
                console.print(
                    "\n[bold red]Partida encerrada.[/bold red]"
                )
                return

            if opc == 1:
                combate = Combate(
                    jog=jogador_atual,
                    jogadores=jogadores,
                )

                combate.atacar()
                partida.verificar_mortos()

                if len(jogadores) > 1:
                    jogador_atual = partida.proximo_jogador(
                        jogador_atual
                    )

            elif opc == 2:
                loja.comprar_equipamentos(jogador_atual)

            elif opc == 3:
                jogador_atual.mostrar_inventario()

        console.print(
            "\n[bold magenta]"
            "Deseja iniciar uma nova partida?"
            "[/bold magenta]"
        )
        console.print("[1] ⚔️ Jogar novamente")
        console.print("[0] 🚪 Encerrar o jogo")

        jogar_novamente = ler_inteiro(
            "Sua opção: ",
            opcoes={0, 1},
        )

        if jogar_novamente == 0:
            console.print(
                "\n[bold cyan]"
                "Obrigado por jogar Fragmentos do Destino!"
                "[/bold cyan]"
            )
            break

        for jogador in todos_jogadores:
            jogador.restaurar_vidas()


if __name__ == "__main__":
    main()
