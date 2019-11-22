import pygame

WIDTH = 800
HEIGHT = 600
FPS = 30
WALL = pygame.image.load('./assets/textures/wall.png')
RESCUE = pygame.image.load('./assets/textures/rescue.png')
MAP_MATRIX = [[1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
              [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
              [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
              [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
              [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
              ]

# definir cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREY = (180,180,180)

# inicialização do jogo
pygame.init()
pygame.mixer.init()  # permite som
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New Flash Gordon")
clock = pygame.time.Clock()

# game loop
running = True
while running:
    clock.tick(FPS)
    # ler eventos
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # atualizar
    
    # render
    screen.fill(BLACK)
    for row in range(8):
        for col in range(30):
            if MAP_MATRIX[row][col] == 0:
                pass
            elif MAP_MATRIX[row][col] == 1:
                screen.blit(WALL, (25+25*col, 375+25*row))
    for x, y in [(380, 405), (330, 505), (260, 480), (80, 460), (85, 535),(115, 410),
                 (710, 435), (660, 460), (530, 430), (535, 510), (560, 485)]:
        screen.blit(RESCUE, (x, y))
    pygame.draw.rect(screen, WHITE, (0,393-25,800,7), 0)
    pygame.draw.rect(screen, GREY, (0,0,25,800), 0)
    pygame.draw.rect(screen, GREY, (0,600-25,800,25), 0)
    pygame.draw.rect(screen, GREY, (800-25,0,25,600), 0)
    pygame.draw.rect(screen, GREY, (0,0,800,75), 0)
            
    pygame.display.flip()

pygame.quit()
