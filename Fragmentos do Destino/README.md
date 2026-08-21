# ⚔️ Fragmentos do Destino

**Fragmentos do Destino** é um jogo de RPG em desenvolvimento, criado em Python para praticar programação orientada a objetos.

Os jogadores participam de batalhas por turnos, realizam ataques definidos por dados, administram moedas e compram equipamentos para fortalecer seus personagens.

## 🎮 Sobre o jogo

No início da partida, os jogadores informam seus nomes e recebem 100 pontos de vida.

Durante seu turno, cada jogador pode:

- ⚔️ Atacar outro jogador
- 🛒 Visitar a loja
- 📦 Consultar seu inventário
- 🗡️ Equipar armas
- 💍 Equipar anéis
- 🚪 Sair da partida

A partida continua enquanto houver mais de um jogador vivo.

## ⚔️ Sistema de combate

O combate utiliza dados para calcular os ataques.

Cada jogador possui:

- Pontos de vida
- Dano base
- Bônus de dano
- Bônus de agilidade
- Arma equipada
- Anel equipado
- Inventário
- Moedas

O resultado dos dados pode influenciar o acerto e o dano causado. Em determinadas condições, o jogador também pode ativar um ataque especial.

## 🛒 Sistema de loja

A loja possui um catálogo compartilhado, permitindo que todos os jogadores tenham acesso aos mesmos equipamentos.

Cada equipamento possui:

- Nome
- Tipo
- Dano
- Agilidade
- Preço

Antes de finalizar uma compra, o jogo verifica se o jogador possui moedas suficientes. Quando a compra é realizada, o valor é descontado e o equipamento é enviado ao inventário.

## 📦 Inventário e equipamentos

Cada jogador possui seu próprio inventário.

Os equipamentos comprados podem ser selecionados e equipados durante a partida. Atualmente, existem dois tipos principais:

- **Armas:** aumentam o dano do jogador
- **Anéis:** podem oferecer bônus de dano ou agilidade

Ao equipar um novo item do mesmo tipo, o equipamento anterior é substituído.

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
└── __main__.py
```

## 🧠 Conceitos aplicados

O projeto utiliza diferentes conceitos da linguagem Python:

- Classes e objetos
- Atributos e métodos
- Programação orientada a objetos
- Composição entre classes
- Pacotes e módulos
- Listas
- Estruturas condicionais
- Laços de repetição
- Funções
- Type hints
- Validação de entradas
- Organização de responsabilidades
- Versionamento com Git e GitHub

## 🎨 Interface

A interface do jogo é exibida no terminal e utiliza a biblioteca **Rich** para apresentar:

- Painéis
- Tabelas
- Cores
- Emojis
- Informações dos jogadores
- Catálogo da loja
- Menus de ações

## 🛠️ Tecnologias utilizadas

- Python
- Rich
- PyCharm
- Git
- GitHub

## 📌 Status do projeto

O projeto está em desenvolvimento e recebe novas funcionalidades conforme o aprendizado evolui.

## 👨‍💻 Autor

Desenvolvido por **Ygor Schiezaro**.

[GitHub — YgorSchiezaro](https://github.com/YgorSchiezaro)