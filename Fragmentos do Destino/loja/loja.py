from equipamento import Equipamento, equipamento
from rich.console import Console
from rich.table import Table
from rich import box
from jogador import Jogador
from entrada import ler_inteiro
console = Console()

class Loja:
    def __init__(self):
        self.catalogo: list[Equipamento] = []
    def cadastrar_equipamento(self, equipamento):
        self.catalogo.append(equipamento)

    def listar_equipamentos(self):
        if not self.catalogo:
            console.print("[bold red]A loja ainda não possui equipamentos.[/bold red]")
            return

        tabela = Table(title=":shopping_cart: LOJA DE EQUIPAMENTOS :shopping_cart:",
                      box = box.ROUNDED,
                      header_style="bold magenta",
                      border_style="bright_blue",
        )
        tabela.add_column("ID", justify="center", style="cyan")
        tabela.add_column(":crossed_swords: Equipamento :crossed_swords:", justify="center", style="bold white")
        tabela.add_column("Tipo", justify="center", style="yellow")
        tabela.add_column("Dano", justify="center", style="red", width=5)
        tabela.add_column("Agilidade", justify="center", style="green")
        tabela.add_column(":money_bag: Preço", justify="center", style="bright_yellow")

        for indice, equipamento in enumerate(self.catalogo, start=1):
            tabela.add_row(
                str(indice),
                equipamento.nome,
                equipamento.tipo,
                str(equipamento.dano),
                str(equipamento.agilidade),
                f"{equipamento.valor} moedas"
            )
        console.print(tabela)

    def comprar_equipamentos(self, jogador: Jogador):
        if not self.catalogo:
            console.print("[bold red]A loja ainda não possui equipamentos.[/bold red]")
            return

        self.listar_equipamentos()

        console.print(f":money_bag: Saldo de [bold]{jogador.nome}[/bold]: :money_bag:"
                      f"[yellow]{jogador.moedas} moedas [/yellow]"
        )
        console.print("[0] Sair da Loja")

        escolha = ler_inteiro(
            "Escolha o equipamento: ",
            minimo= 0,
            maximo = len(self.catalogo),
        )
        if escolha == 0:
            console.print(":door Saindo da Loja...")
            return
        equipamento_escolhido = self.catalogo[escolha - 1]

        if not jogador.gastar_moedas(equipamento_escolhido.valor):
            return

        equipamento_comprado = Equipamento(
            nome = equipamento_escolhido.nome,
            dano = equipamento_escolhido.dano,
            valor= equipamento_escolhido.valor,
            agilidade= equipamento_escolhido.agilidade,
            tipo= equipamento_escolhido.tipo,
        )

        jogador.adicionar_item_inventario(equipamento_comprado)




