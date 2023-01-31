import random
import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
from sprites import Input

def palavras (tamanhostring):
    sorteio=""
    for i in range(tamanhostring):
        sorteio+=str(random.randint(0,9))
    return sorteio

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    #renderizando texto
    font = pygame.font.SysFont(None, 48)

    DONE = 0
    PLAYING = 1
    state = PLAYING
    last_update = pygame.time.get_ticks()
    imgprincipal = Input(dicionario_de_arquivos,palavras(2))

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)
        segundos = int(pygame.time.get_ticks() - last_update)
        print(segundos)


        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor PRETA
        window.blit(imgprincipal.image, imgprincipal.rect)
        text = font.render(imgprincipal.palavra, True, (0, 0, 255))
        window.blit(text, (430, 250))
        text = font.render("MEMORIZE", True, (0, 0, 255))
        window.blit(text, (350, 170))


        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
