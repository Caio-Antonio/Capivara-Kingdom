import pygame
import os

# Inicializa o Pygame
pygame.init()

# Configura a janela do jogo
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Carrega as imagens
imagens = []
for i in range(0, 7):
    imagem_path = os.path.join("/Users/caio/Developer/DS/capivara/", f"inimigo_atacando({i}).png")
    imagem = pygame.image.load(imagem_path)
    imagem = pygame.transform.scale(imagem, (imagem.get_width() * 4, imagem.get_height() * 4))  # Aumenta o tamanho da imagem
    imagens.append(imagem)

# Configura as variáveis
indice_imagem = 0
tempo_animacao = 200  # Tempo em milissegundos para cada imagem
tempo_atual = pygame.time.get_ticks()

# Loop principal do jogo
jogando = True
while jogando:
    # Processa os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False

    # Verifica se é hora de trocar de imagem
    if pygame.time.get_ticks() - tempo_atual > tempo_animacao:
        indice_imagem = (indice_imagem + 1) % len(imagens)  # Alterna entre as imagens
        tempo_atual = pygame.time.get_ticks()

    # Limpa a tela
    screen.fill((255, 255, 255))

    # Desenha a imagem atual na tela
    imagem_atual = imagens[indice_imagem]
    screen.blit(imagem_atual, (WIDTH // 2 - imagem_atual.get_width() // 2, HEIGHT // 2 - imagem_atual.get_height() // 2))

    # Atualiza a tela
    pygame.display.flip()

    # Limita a taxa de quadros
    clock.tick(60)

# Encerra o Pygame
pygame.quit()
