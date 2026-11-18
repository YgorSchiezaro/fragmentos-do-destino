from collections.abc import Collection


def ler_inteiro(
    mensagem: str,
    minimo: int | None = None,
    maximo: int | None = None,
    opcoes: Collection[int] | None = None,
) -> int:
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro.")
            continue

        if minimo is not None and valor < minimo:
            print(f"Digite um número maior ou igual a {minimo}.")
            continue

        if maximo is not None and valor > maximo:
            print(f"Digite um número menor ou igual a {maximo}.")
            continue

        if opcoes is not None and valor not in opcoes:
            opcoes_formatadas = ", ".join(str(opcao) for opcao in sorted(opcoes))
            print(f"Escolha uma das opções: {opcoes_formatadas}.")
            continue

        return valor
