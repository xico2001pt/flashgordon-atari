import pygame

WIDTH = 800
HEIGHT = 600
FPS = 30

# load
# ICON = pygame.image.load('./assets/textures/icon.png')
RESCUE = pygame.image.load('./assets/textures/rescue.png')
SPACESHIP = pygame.image.load('./assets/textures/spaceship.png')
rescue_points = [(380, 405), (330, 505), (260, 480), (80, 460), (85, 535), (115, 410),
                 (710, 435), (660, 460), (530, 430), (535, 510), (560, 485)]
MAP_MATRIX = [[1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
              [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
              [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
              [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
              [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]]
# physics
XS0, YS0 = 350, 200
XIS0, YIS0 = 395, 485
xs, ys = XS0, YS0
xis, yis = XIS0, YIS0
SPACESHIP_VEL = 0.15
SPACESHIP_ICON_VEL = 0.02
right_side = True

# definir cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
BLUE = (0, 85, 212)
BROWN = (170, 100, 30)

# inicialização do jogo
pygame.init()
pygame.mixer.init()  # permite som
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New Flash Gordon")
# pygame.display.set_icon(ICON)
clock = pygame.time.Clock()

# game loop
running = True
while running:
    dt = clock.tick(FPS)
    
    # ler eventos
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        ys -= SPACESHIP_VEL * dt
        yis -= SPACESHIP_ICON_VEL * dt
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        ys += SPACESHIP_VEL * dt
        yis += SPACESHIP_ICON_VEL * dt
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        xs -= SPACESHIP_VEL * dt * 1.5
        xis -= SPACESHIP_ICON_VEL * dt * 1.5
        right_side = False
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        xs += SPACESHIP_VEL * dt * 1.5
        xis += SPACESHIP_ICON_VEL * dt * 1.5
        right_side = True
    if keys[pygame.K_SPACE]:
        xs, ys = XS0, YS0
        xis, yis = XIS0, YIS0

    # atualizar
    spaceship_pos = (xs, ys)
    
    # render
    screen.fill(BLACK)
    for row in range(8):
        for col in range(30):
            if MAP_MATRIX[row][col]:
                pygame.draw.rect(screen, BROWN, (25+25*col, 375+25*row, 25, 25), 0)
    for x, y in rescue_points:
        screen.blit(RESCUE, (x, y))
    if right_side:
        screen.blit(SPACESHIP, spaceship_pos)
    else:
        screen.blit(pygame.transform.flip(SPACESHIP, True, False), spaceship_pos)
    pygame.draw.rect(screen, BLUE, (xis,yis,10,5), 0)
    
    # consola
    pygame.draw.rect(screen, WHITE, (0,393-25,800,7), 0)
    pygame.draw.rect(screen, GREY, (0,0,25,800), 0)
    pygame.draw.rect(screen, GREY, (0,600-25,800,25), 0)
    pygame.draw.rect(screen, GREY, (800-25,0,25,600), 0)
    pygame.draw.rect(screen, GREY, (0,0,800,75), 0)
            
    pygame.display.flip()

pygame.quit()
