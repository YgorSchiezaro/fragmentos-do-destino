import pygame

resolucao_logica = (320, 180)
escala = 3

tamanho_janela = (
    resolucao_logica[0] * escala,
    resolucao_logica[1] * escala,
)

COR_FUNDO = (25, 22, 35)
COR_PAINEL = (242, 224, 186)
COR_BORDA = (25, 22, 35)
COR_VIDA = (88, 158, 96)
COR_VIDA_BAIXA = (190, 67, 71)
COR_TEXTO = (25, 22, 35)

def desenhar_barra_vida(tela, x, y, vida_atual, vida_maxima):
    largura = 100
    altura = 10

    pygame.draw.rect(tela, COR_BORDA, (x, y, largura, altura))
    porcentagem_vida = vida_atual / vida_maxima
    largura_vida = int((largura - 2) * porcentagem_vida)
    cor_vida = COR_VIDA

    if porcentagem_vida <= 0.3:
        cor_vida = COR_VIDA_BAIXA

    pygame.draw.rect(tela, cor_vida, (x + 1, y +1, largura_vida, altura - 2))

def desenhar_personagem(tela, x, y, cor_roupa):
    cor_pele = (238, 186, 139)

    #cabeça
    pygame.draw.rect(tela, COR_BORDA, (x + 5, y, 10, 10))
    pygame.draw.rect(tela, cor_pele, (x + 6, y + 4, 8, 6))

    #corpo
    pygame.draw.rect(tela, cor_roupa, (x + 4, y + 10, 12, 12))

    # Pernas
    pygame.draw.rect(tela, COR_BORDA, (x + 4, y + 22, 5, 6))
    pygame.draw.rect(tela, COR_BORDA, (x + 11, y + 22, 5, 6))

    # Espada
    pygame.draw.rect(tela, (242, 190, 77), (x + 16, y + 12, 8, 2))

def main():
    pygame.init()
    janela = pygame.display.set_mode(tamanho_janela)
    pygame.display.set_caption("Fragmentos do Destino")

    tela = pygame.Surface(resolucao_logica)
    relogio = pygame.time.Clock()

    fonte = pygame.font.Font(None, 14)
    fonte_titulo = pygame.font.Font(None, 20)

    executando = True

    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        tela.fill(COR_FUNDO)

        painel_status = pygame.Rect(10, 10, 300, 43)
        pygame.draw.rect(tela, COR_PAINEL, painel_status)
        pygame.draw.rect(tela, COR_BORDA, painel_status, width= 2)

        titulo = fonte_titulo.render("Fragmentos do Destino", False, COR_TEXTO)

        tela.blit(titulo, (77, 16))
        nome_jogador_1 = fonte.render("Jogador 1", False, COR_TEXTO)
        nome_jogador_2 = fonte.render("Jogador 2", False, COR_TEXTO)

        tela.blit(nome_jogador_1, (20, 35))
        tela.blit(nome_jogador_2, (220, 35))

        desenhar_barra_vida(tela, 20, 43, vida_atual=100, vida_maxima=100)
        desenhar_barra_vida(tela, 200, 43, vida_atual=65, vida_maxima=100)

        desenhar_personagem(tela, 65, 85, (137, 91, 166))
        desenhar_personagem(tela, 235, 85, (190, 67, 71))

        painel_mensagem = pygame.Rect(10, 135, 300, 32)
        pygame.draw.rect(tela, COR_PAINEL, painel_mensagem)
        pygame.draw.rect(tela, COR_BORDA, painel_mensagem, width=2)

        mensagem = fonte.render(
            "Uma batalha se aproxima...",
            False,
            COR_TEXTO,
        )
        tela.blit(mensagem, (18, 146))

        pygame.transform.scale(tela, tamanho_janela, janela)
        pygame.display.flip()
        relogio.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
