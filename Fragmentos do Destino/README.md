# ⚔️ Fragmentos do Destino

**Fragmentos do Destino** é um RPG por turnos em desenvolvimento, criado em Python como projeto de prática de programação orientada a objetos.

O jogo começou como uma experiência de terminal e está sendo preparado para receber uma interface gráfica em pixel art com Pygame Community Edition.

Os jogadores participam de batalhas por turnos, usam dados para atacar, administram moedas e compram equipamentos para fortalecer seus personagens.

## 🎮 Sobre o jogo

No início da partida, cada jogador possui:

- 100 pontos de vida;
- 0 moedas, exceto o primeiro jogador, que inicia com moedas de teste;
- Inventário vazio;
- Nenhuma arma ou anel equipado.

Atualmente, os jogadores recebem nomes padrão, como `Jogador 1` e `Jogador 2`.

Durante seu turno, cada jogador pode:

- ⚔️ Atacar outro jogador;
- 🛒 Visitar a loja;
- 📦 Consultar o inventário;
- 🗡️ Equipar armas;
- 💍 Equipar anéis;
- 🚪 Sair da partida.

A partida continua enquanto houver mais de um jogador vivo.

## ⚔️ Sistema de combate

O combate funciona por turnos e usa três dados:

| Dado | Função |
|---|---|
| d20 de agilidade | Define se o ataque acerta |
| d10 de ataque | Define o dano base |
| d10 de sorte | Pode ativar um ataque especial |

O fluxo de um ataque é:

1. O jogador rola o d20 de agilidade.
2. O bônus de agilidade do anel equipado é somado ao resultado.
3. Se a agilidade total for maior que 10, o ataque acerta.
4. O jogador rola o d10 de ataque e o d10 de sorte.
5. O dano recebe bônus de arma, anel e dano base.
6. O dano é dobrado em caso de ataque especial.

Um ataque especial é ativado quando:

- A agilidade total é maior ou igual a 20; ou
- O dado de sorte resulta em 10.

### Exemplo de ataque

```text
Dado de agilidade: 8
Bônus do anel: +4
Agilidade total: 12
```

Como `12` é maior que `10`, o ataque acerta.

```text
Dado de ataque: 5
Dano da espada: +5
Dano do anel: +1
Dano total: 11
```

Se houver ataque especial:

```text
11 × 2 = 22 de dano
```

## 🛒 Sistema de loja

A loja possui um catálogo compartilhado. Todos os jogadores podem comprar os mesmos equipamentos.

Cada equipamento possui:

- Nome;
- Tipo;
- Dano;
- Agilidade;
- Preço.

Antes de concluir uma compra, o jogo verifica se o jogador possui moedas suficientes. Se a compra for válida, as moedas são descontadas e o item é enviado ao inventário.

### Equipamentos atuais

| Equipamento | Tipo | Dano | Agilidade | Preço |
|---|---:|---:|---:|---:|
| Espada de Pedra | Arma | +5 | +0 | 8 moedas |
| Espada de Ferro | Arma | +10 | +0 | 12 moedas |
| Anel Mágico | Anel | +1 | +4 | 5 moedas |
| Anel da Agilidade | Anel | +0 | +6 | 7 moedas |

## 📦 Inventário e equipamentos

Cada jogador possui um inventário próprio.

Os itens comprados podem ser equipados durante a partida.

- **Armas:** aumentam o dano causado.
- **Anéis:** podem aumentar o dano, a agilidade ou os dois atributos.

Um jogador pode equipar:

- Uma arma;
- Um anel.

Ao equipar um novo item do mesmo tipo, o equipamento anterior é substituído.

## 🎨 Interface

### Terminal

A versão principal do jogo funciona no terminal e utiliza a biblioteca **Rich** para apresentar:

- Painéis;
- Tabelas;
- Cores;
- Emojis;
- Informações dos jogadores;
- Catálogo da loja;
- Menus de ações.

### Pixel art — em desenvolvimento

O projeto possui uma primeira base para a futura interface gráfica em pixel art.

O arquivo `jogo_pixel.py` usa:

- Resolução lógica de `320 × 180`;
- Escala de `3x`;
- Janela final de `960 × 540`;
- Pygame Community Edition;
- Painéis, barras de vida e personagens provisórios desenhados com retângulos.

Os personagens atuais são apenas protótipos. Posteriormente, serão substituídos por sprites pixel art, animações, botões e telas conectadas ao combate real.

## 🗂️ Estrutura do projeto

```text
Fragmentos do Destino/
├── combate/
│   ├── __init__.py
│   └── combate.py
├── equipamento/
│   ├── __init__.py
│   └── equipamento.py
├── jogador/
│   ├── __init__.py
│   └── jogador.py
├── loja/
│   ├── __init__.py
│   └── loja.py
├── partida/
│   ├── __init__.py
│   └── partida.py
├── entrada.py
├── jogo_pixel.py
├── requirements.txt
└── __main__.py
```

## 🧠 Conceitos aplicados

O projeto utiliza conceitos importantes de Python:

- Classes e objetos;
- Atributos e métodos;
- Programação orientada a objetos;
- Composição entre classes;
- Pacotes e módulos;
- Listas;
- Estruturas condicionais;
- Laços de repetição;
- Funções;
- Type hints;
- Validação de entradas;
- Organização de responsabilidades;
- Separação entre lógica do jogo e interface;
- Eventos e loop de jogo com Pygame;
- Versionamento com Git e GitHub.

## 🛠️ Tecnologias utilizadas

- Python;
- Rich;
- Pygame Community Edition (`pygame-ce`);
- PyCharm;
- Git;
- GitHub.

## ▶️ Como executar

Clone o repositório:

```powershell
git clone https://github.com/YgorSchiezaro/fragmentos-do-destino.git
cd "fragmentos-do-destino"
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

Execute a versão de terminal:

```powershell
python __main__.py
```

Execute a primeira tela pixel art:

```powershell
python jogo_pixel.py
```

> Mesmo instalando `pygame-ce`, o código Python continua usando:
>
> ```python
> import pygame
> ```

## 📌 Status do projeto

O jogo está em desenvolvimento.

Próximas etapas planejadas:

- [x] Sistema de combate por turnos;
- [x] Loja, inventário e equipamentos;
- [x] Bônus de dano e agilidade;
- [x] Base da janela pixel art;
- [ ] Botões clicáveis;
- [ ] Conectar a interface Pygame ao combate real;
- [ ] Sprites pixel art;
- [ ] Animações de ataque;
- [ ] Sons e música;
- [ ] Mapas e exploração.
